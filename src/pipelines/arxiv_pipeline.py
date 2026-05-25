"""ArXiv pipeline: fetch → dedup → h-index filter → LLM score → LLM insights → DB."""

import json
import os
import re
import time
from datetime import datetime, timedelta
from html import unescape
from pathlib import Path
from typing import Dict, List

import feedparser
import requests

from ..db import database
from ..llm import client as llm_client
from ..llm.prompts import INSIGHTS_PROMPT
from ..llm.scoring import score_papers_batch

# ---------------------------------------------------------------------------
# ArXiv RSS fetch
# ---------------------------------------------------------------------------


def fetch_arxiv_rss(category: str) -> List[Dict]:
    """Fetch new papers from the ArXiv RSS feed for a single category."""
    updated = datetime.utcnow() - timedelta(days=1)
    updated_str = updated.strftime("%a, %d %b %Y %H:%M:%S GMT")
    feed = feedparser.parse(
        f"http://export.arxiv.org/rss/{category}",
        modified=updated_str,
    )
    if getattr(feed, "status", 200) == 304:
        print(f"  No new papers for {category}")
        return []

    papers = []
    for entry in feed.entries:
        if entry.get("arxiv_announce_type", "new") != "new":
            continue
        arxiv_id = entry.link.split("/")[-1]
        authors_raw = entry.get("author", "")
        authors = [
            unescape(re.sub("<[^<]+?>", "", a)).strip()
            for a in authors_raw.replace("\n", ", ").split(",")
            if a.strip()
        ]
        abstract = unescape(re.sub("<[^<]+?>", "", entry.get("summary", "")).replace("\n", " "))
        title = re.sub(r"\(arXiv:[0-9.]+v[0-9]+ \[.*?\]\)$", "", entry.title).strip()
        published = entry.get("published", "")[:10]
        papers.append(
            {
                "arxiv_id": arxiv_id,
                "title": title,
                "authors": ", ".join(authors),
                "abstract": abstract,
                "categories": category,
                "published_date": published,
            }
        )
    return papers


# ---------------------------------------------------------------------------
# Semantic Scholar helpers
# ---------------------------------------------------------------------------


def _s2_headers(api_key: str) -> Dict:
    return {"X-API-KEY": api_key} if api_key else {}


def fetch_author_hindex(author_names: List[str], api_key: str) -> Dict[str, int]:
    """Return {author_name: max_hIndex} from Semantic Scholar author search."""
    hindex_map: Dict[str, int] = {}
    session = requests.Session()
    sleep_sec = 0.05 if api_key else 1.0
    for name in author_names:
        try:
            resp = session.get(
                "https://api.semanticscholar.org/graph/v1/author/search",
                params={"query": name, "fields": "authorId,name,hIndex", "limit": "5"},
                headers=_s2_headers(api_key),
                timeout=10,
            )
            resp.raise_for_status()
            data = resp.json().get("data", [])
            if data:
                hindex_map[name] = max((a.get("hIndex") or 0 for a in data), default=0)
        except Exception as e:
            print(f"  S2 lookup failed for '{name}': {e}")
        time.sleep(sleep_sec)
    return hindex_map


def filter_by_hindex(papers: List[Dict], hindex_map: Dict[str, int], cutoff: int) -> List[Dict]:
    """Keep papers where at least one author has h-index >= cutoff."""
    result = []
    for paper in papers:
        authors = [a.strip() for a in paper["authors"].split(",")]
        max_h = max((hindex_map.get(a, 0) for a in authors), default=0)
        if max_h >= cutoff:
            result.append(paper)
    return result


def load_watched_author_ids(authors_txt: Path) -> set:
    """Load Semantic Scholar author IDs from authors.txt (name, s2_id per line)."""
    ids = set()
    if not authors_txt.exists():
        return ids
    for line in authors_txt.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(",")
        if len(parts) >= 2:
            ids.add(parts[1].strip())
    return ids


# ---------------------------------------------------------------------------
# Papers With Code — code repo lookup
# ---------------------------------------------------------------------------


def find_code_repo(arxiv_id: str) -> str:
    """Query Papers With Code for the top code repository of a paper.

    Returns the GitHub URL (most-starred, official preferred) or empty string.
    """
    clean_id = re.sub(r"v\d+$", "", arxiv_id)  # strip version suffix e.g. 2301.07543v2
    try:
        resp = requests.get(
            "https://paperswithcode.com/api/v1/papers/",
            params={"arxiv_id": clean_id},
            timeout=8,
        )
        resp.raise_for_status()
        results = resp.json().get("results", [])
        if not results:
            return ""
        pwc_id = results[0]["id"]
        repo_resp = requests.get(
            f"https://paperswithcode.com/api/v1/papers/{pwc_id}/repositories/",
            timeout=8,
        )
        repo_resp.raise_for_status()
        repos = repo_resp.json().get("results", [])
        if not repos:
            return ""
        # Prefer official repos; within each group sort by stars descending
        official = [r for r in repos if r.get("is_official")]
        pool = official if official else repos
        pool.sort(key=lambda r: r.get("stars", 0), reverse=True)
        return pool[0].get("url", "")
    except Exception as e:
        print(f"  PWC lookup failed for {arxiv_id}: {e}")
        return ""


# ---------------------------------------------------------------------------
# LLM insights
# ---------------------------------------------------------------------------


def generate_insights(paper: Dict) -> Dict:
    """Call LLM to produce a structured insight block for one paper."""
    prompt = INSIGHTS_PROMPT.format(
        title=paper["title"],
        authors=paper["authors"],
        abstract=paper["abstract"][:3000],
    )
    try:
        raw = llm_client.complete(prompt)
        raw = re.sub(r"```json\n?", "", raw)
        raw = re.sub(r"```", "", raw).strip()
        return json.loads(raw)
    except Exception as e:
        print(f"  Insights failed for {paper['arxiv_id']}: {e}")
        return {}


# ---------------------------------------------------------------------------
# Pipeline entry point
# ---------------------------------------------------------------------------


def run(config: dict) -> List[Dict]:
    """Execute the full ArXiv pipeline and return saved papers."""
    arxiv_cfg = config["arxiv"]
    categories: List[str] = arxiv_cfg["categories"]
    hindex_cutoff: int = arxiv_cfg.get("hindex_cutoff", 10)
    relevance_cutoff: int = arxiv_cfg.get("relevance_cutoff", 2)
    max_papers: int = arxiv_cfg.get("max_papers_per_day", 30)
    interests: str = arxiv_cfg.get(
        "interests",
        "AI, machine learning, computer vision, robotics, NLP",
    )
    topic_categories: List[str] = config["topic_categories"]
    s2_key: str = os.environ.get("SEMANTIC_SCHOLAR_KEY", "")

    authors_txt = Path(__file__).parent.parent / "configs" / "authors.txt"
    watched_ids = load_watched_author_ids(authors_txt)

    # 1. Fetch from all categories, deduplicate across categories
    seen_ids: set = set()
    all_papers: List[Dict] = []
    for cat in categories:
        for paper in fetch_arxiv_rss(cat.strip()):
            if paper["arxiv_id"] not in seen_ids:
                seen_ids.add(paper["arxiv_id"])
                all_papers.append(paper)
    print(f"Fetched {len(all_papers)} papers from ArXiv RSS")

    # 2. Skip already-processed papers
    new_papers = [p for p in all_papers if not database.paper_exists(p["arxiv_id"])]
    print(f"{len(new_papers)} new (not in DB)")
    if not new_papers:
        return []

    # 3. H-index filter via Semantic Scholar
    all_authors = list({a.strip() for p in new_papers for a in p["authors"].split(",")})
    print(f"Fetching h-index for {len(all_authors)} authors...")
    hindex_map = fetch_author_hindex(all_authors, s2_key)
    new_papers = filter_by_hindex(new_papers, hindex_map, hindex_cutoff)
    print(f"{len(new_papers)} papers pass h-index filter (>= {hindex_cutoff})")
    if not new_papers:
        return []

    # 4. LLM pass 1: relevance scoring (batched)
    print("Scoring papers for relevance...")
    scores = score_papers_batch(new_papers, topic_categories, interests)

    # 5. Apply watched-author boost, filter below cutoff
    scored: List[Dict] = []
    for paper in new_papers:
        score_data = scores.get(paper["arxiv_id"], {})
        relevance = int(score_data.get("relevance", 1))
        # Boost papers by watched authors
        if watched_ids:
            authors = [a.strip() for a in paper["authors"].split(",")]
            if any(a in watched_ids for a in authors):
                relevance = max(relevance, 3)
        if relevance < relevance_cutoff:
            continue
        paper["relevance"] = relevance
        paper["topic_category"] = score_data.get("topic_category", "")
        scored.append(paper)

    print(f"{len(scored)} papers pass relevance cutoff (>= {relevance_cutoff})")
    scored = scored[:max_papers]

    # 6. Check Papers With Code for code availability
    print("Checking Papers With Code for code repos...")
    for paper in scored:
        paper["code_url"] = find_code_repo(paper["arxiv_id"])
        if paper["code_url"]:
            print(f"  Code: {paper['arxiv_id']} → {paper['code_url']}")
        time.sleep(0.2)  # be polite to PWC API

    # 7. LLM pass 2: generate insights per paper
    for paper in scored:
        print(f"  Insights: {paper['title'][:60]}...")
        paper["insights"] = generate_insights(paper)

    # 8. Write to SQLite
    for paper in scored:
        database.upsert_paper(paper)
    print(f"Saved {len(scored)} papers to database")

    return scored
