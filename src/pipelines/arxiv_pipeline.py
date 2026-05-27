"""ArXiv pipeline: fetch -> dedup -> LLM score -> LLM insights -> DB."""

import logging
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta
from html import unescape
from typing import Dict, List

import feedparser
from tqdm import tqdm

from ..db import database
from ..llm import client as llm_client
from ..llm.prompts import INSIGHTS_PROMPT
from ..llm.scoring import parse_json_response, score_papers_batch

logger = logging.getLogger(__name__)

MAX_WORKERS = 4

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _get_entry_categories(entry, fallback: str = "") -> str:
    """Return space-joined, deduplicated ArXiv category codes from a feed entry."""
    cats = []
    for tag in entry.get("tags", []):
        term = tag.get("term", "")
        if term and "." in term:  # ArXiv codes always contain a dot
            cats.append(term)
    if not cats:
        primary = entry.get("category", fallback)
        if primary:
            cats = [primary]
    seen, unique = set(), []
    for c in cats:
        if c not in seen:
            seen.add(c)
            unique.append(c)
    return " ".join(unique) or fallback


# ---------------------------------------------------------------------------
# ArXiv RSS fetch  (subject-based — global trends)
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
        logger.info("No new papers for %s", category)
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
        pub_raw = entry.get("published", "")
        try:
            published = datetime.strptime(pub_raw[:10], "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            published = datetime.utcnow().strftime("%Y-%m-%d")
        categories = _get_entry_categories(entry, fallback=category)
        papers.append(
            {
                "arxiv_id": arxiv_id,
                "title": title,
                "authors": ", ".join(authors),
                "abstract": abstract,
                "categories": categories,
                "published_date": published,
                "discovery_type": "subject",
                "search_topic": "",
            }
        )
    return papers


# ---------------------------------------------------------------------------
# ArXiv keyword search  (topic-based — personalized discovery)
# ---------------------------------------------------------------------------


def fetch_arxiv_by_topic(topic: str, days_back: int = 3, max_results: int = 20) -> List[Dict]:
    """Search ArXiv for recent papers matching a user interest topic.

    Uses targeted ti:/abs: phrase search + submittedDate range filter to keep
    result sets small and avoid rate-limiting (HTTP 429).

    API docs: https://info.arxiv.org/help/api/user-manual.html#query_details
    Equivalent browser URL: https://arxiv.org/search/?query=<topic>&searchtype=all
    """
    # Quoted phrase in title OR abstract — much more precise than all:topic.
    # Spaces become +, quotes URL-encoded as %22, parens as %28/%29.
    topic_safe = topic.replace(" ", "+")
    phrase = f"%22{topic_safe}%22"

    # submittedDate range in YYYYMMDDTTTT format (TTTT = HHMM, GMT)
    date_from = (datetime.utcnow() - timedelta(days=days_back)).strftime("%Y%m%d0000")
    date_to = datetime.utcnow().strftime("%Y%m%d2359")

    search_query = (
        f"%28ti:{phrase}+OR+abs:{phrase}%29" f"+AND+submittedDate:[{date_from}+TO+{date_to}]"
    )
    url = (
        f"https://export.arxiv.org/api/query"
        f"?search_query={search_query}"
        f"&sortBy=submittedDate&sortOrder=descending"
        f"&max_results={max_results}"
    )

    # ArXiv requests >= 3 s between consecutive API calls
    time.sleep(3)

    def _call():
        try:
            return feedparser.parse(url)
        except Exception as e:
            logger.warning("Network error for '%s': %s", topic, e)
            return None

    feed = _call()
    if feed is None:
        return []

    status = getattr(feed, "status", 200)
    if status == 429:
        logger.warning("Rate-limited (429) for '%s', waiting 60s then retrying...", topic)
        time.sleep(60)
        feed = _call()
        if feed is None:
            return []
        status = getattr(feed, "status", 200)

    if status not in (200, 304):
        logger.warning("ArXiv API returned HTTP %d for '%s', skipping", status, topic)
        return []

    cutoff = (datetime.utcnow() - timedelta(days=days_back)).strftime("%Y-%m-%d")
    papers = []
    for entry in feed.entries:
        # Atom id looks like https://arxiv.org/abs/2605.12345v1
        arxiv_id = entry.get("id", "").rstrip("/").split("/")[-1].split("v")[0]
        if not arxiv_id:
            continue

        pub_raw = entry.get("published", "")
        try:
            published = datetime.strptime(pub_raw[:10], "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            published = datetime.utcnow().strftime("%Y-%m-%d")

        # Belt-and-suspenders: API date filter handles most, but double-check
        if published < cutoff:
            continue

        categories = _get_entry_categories(entry, fallback="cs.AI")

        if entry.get("authors"):
            authors = ", ".join(a.get("name", "") for a in entry.authors)
        else:
            authors = unescape(re.sub("<[^<]+?>", "", entry.get("author", ""))).strip()

        abstract = unescape(re.sub("<[^<]+?>", "", entry.get("summary", "")).replace("\n", " "))
        title = unescape(re.sub("<[^<]+?>", "", entry.get("title", ""))).strip()

        papers.append(
            {
                "arxiv_id": arxiv_id,
                "title": title,
                "authors": authors,
                "abstract": abstract,
                "categories": categories,
                "published_date": published,
                "discovery_type": "topic",
                "search_topic": topic,
            }
        )
    return papers


# ---------------------------------------------------------------------------
# Code detection — scan abstract for GitHub URLs
# ---------------------------------------------------------------------------

_GITHUB_URL_RE = re.compile(
    r"https?://github\.com/[\w][\w.-]*/[\w][\w.-]*(?:/[\w./-]*)?",
    re.IGNORECASE,
)
# Characters that should never end a URL when extracted from prose
_URL_TRAILING_JUNK = re.compile(r"[.\,;:!?\)\]>\"\']+$")


def find_code_repo(abstract: str) -> str:
    """Return the first valid GitHub URL found in the abstract, or empty string."""
    match = _GITHUB_URL_RE.search(abstract)
    if not match:
        return ""
    url = _URL_TRAILING_JUNK.sub("", match.group(0))
    # Basic validation: must have a non-empty owner and repo segment
    parts = url.rstrip("/").split("/")  # ['https:', '', 'github.com', owner, repo, ...]
    if len(parts) < 5 or not parts[3] or not parts[4]:
        return ""
    return url


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
        return parse_json_response(llm_client.complete(prompt))
    except Exception as e:
        logger.warning("Insights failed for %s: %s", paper["arxiv_id"], e)
        return {}


# ---------------------------------------------------------------------------
# Pipeline entry point
# ---------------------------------------------------------------------------


def run(config: dict) -> List[Dict]:
    """Execute the full ArXiv pipeline and return saved papers."""
    arxiv_cfg = config["arxiv"]
    categories: List[str] = arxiv_cfg["categories"]
    topic_interests: List[str] = arxiv_cfg.get("topic_interests", [])
    relevance_cutoff: int = arxiv_cfg.get("relevance_cutoff", 2)
    max_papers: int = arxiv_cfg.get("max_papers_per_day", 30)
    max_topic_papers: int = arxiv_cfg.get("max_topic_papers", 10)
    days_back: int = arxiv_cfg.get("days_back", 3)
    interests: str = arxiv_cfg.get(
        "interests",
        "AI, machine learning, computer vision, robotics, NLP",
    )
    topic_categories: List[str] = config["topic_categories"]

    # ── 1. Subject-based fetch (RSS, global trends) ──────────────────────────
    seen_ids: set = set()
    all_papers: List[Dict] = []
    for cat in categories:
        for paper in fetch_arxiv_rss(cat.strip()):
            if paper["arxiv_id"] not in seen_ids:
                seen_ids.add(paper["arxiv_id"])
                all_papers.append(paper)
    logger.info("Fetched %d papers from ArXiv RSS (subjects)", len(all_papers))

    # ── 2. Topic-based fetch (search API, personalized) ──────────────────────
    topic_papers_raw: List[Dict] = []
    if topic_interests:
        logger.info("Searching ArXiv for %d interest topics...", len(topic_interests))
        for topic in topic_interests:
            results = fetch_arxiv_by_topic(
                topic, days_back=days_back, max_results=max_topic_papers
            )
            added = 0
            for paper in results:
                if paper["arxiv_id"] not in seen_ids:
                    seen_ids.add(paper["arxiv_id"])
                    topic_papers_raw.append(paper)
                    added += 1
            logger.info("  '%s': %d new papers", topic, added)
        logger.info("Fetched %d papers from topic search", len(topic_papers_raw))
        all_papers.extend(topic_papers_raw)

    # ── 3. Dedup against DB ──────────────────────────────────────────────────
    new_papers = [p for p in all_papers if not database.paper_exists(p["arxiv_id"])]
    logger.info("%d new (not in DB)", len(new_papers))
    if not new_papers:
        return []

    # ── 4. Recency filter (subject papers only; topic search already filtered) ─
    date_cutoff = (datetime.utcnow() - timedelta(days=days_back)).strftime("%Y-%m-%d")
    new_papers = [
        p
        for p in new_papers
        if p.get("discovery_type") == "topic" or p.get("published_date", "") >= date_cutoff
    ]
    print(f"{len(new_papers)} papers within last {days_back} days (since {date_cutoff})")
    if not new_papers:
        return []

    # ── 5. LLM pass 1: relevance scoring (subject papers) ───────────────────
    subject_papers = [p for p in new_papers if p.get("discovery_type") != "topic"]
    topic_p = [p for p in new_papers if p.get("discovery_type") == "topic"]

    scored: List[Dict] = []

    if subject_papers:
        logger.info("Scoring subject papers for relevance...")
        scores = score_papers_batch(subject_papers, topic_categories, interests)
        for paper in subject_papers:
            score_data = scores.get(paper["arxiv_id"], {})
            relevance = int(score_data.get("relevance", 1))
            if relevance < relevance_cutoff:
                continue
            paper["relevance"] = relevance
            paper["topic_category"] = score_data.get("topic_category", "General")
            scored.append(paper)
        logger.info(
            "%d subject papers pass relevance cutoff (>= %d)", len(scored), relevance_cutoff
        )
        scored = scored[:max_papers]

    # Topic papers: use search topic as category; assign default relevance
    for paper in topic_p:
        paper["relevance"] = 3  # implicit relevance (user chose the topic)
        paper["topic_category"] = paper.get("search_topic", "General")
        scored.append(paper)

    # ── 6. Detect code repos from abstract ──────────────────────────────────
    for paper in scored:
        paper["code_url"] = find_code_repo(paper.get("abstract", ""))
        if paper["code_url"]:
            logger.info("Code: %s -> %s", paper["arxiv_id"], paper["code_url"])

    # -- 7. LLM pass 2: generate insights (concurrent) -----------------------
    llm_client.try_init()
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {pool.submit(generate_insights, p): p for p in scored}
        for future in tqdm(as_completed(futures), total=len(scored), desc="Generating insights"):
            paper = futures[future]
            try:
                paper["insights"] = future.result()
            except Exception as e:
                logger.warning("Insights failed for %s: %s", paper["arxiv_id"], e)
                paper["insights"] = {}

    # ── 8. Write to SQLite ───────────────────────────────────────────────────
    for paper in tqdm(scored, desc="Saving to database"):
        database.upsert_paper(paper)
    logger.info("Saved %d papers to database", len(scored))

    return scored
