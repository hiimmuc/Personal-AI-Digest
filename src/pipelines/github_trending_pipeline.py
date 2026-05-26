"""GitHub Trending repository pipeline.

Flow:
    gtrending.fetch_repos(since="daily", language=lang)
        ↓
    Filter archived=True repos out
        ↓
    GitHub API enrichment (topics, pushed_at, description)
        ↓
    Stage 1: keyword match against interests → drop misses
        ↓
    Stage 2: LLM relevance score (1–5) + README fallback → drop below cutoff
        ↓
    Sort by pushed_at descending
        ↓
    Write to news_items table with source="GitHub Trending"
"""

from __future__ import annotations

import base64
import json
import os
import re
import time
from datetime import date
from typing import Dict, List, Optional

import requests

from ..db import database
from ..llm import client as llm_client
from ..llm.prompts import GITHUB_TRENDING_PROMPT

_GH_API = "https://api.github.com"
_README_MAX_CHARS = 3000  # chars sent to LLM when description is thin


# ── GitHub REST helpers ────────────────────────────────────────────────────────


def _gh_headers() -> Dict[str, str]:
    token = os.environ.get("GITHUB_TOKEN", "")
    headers = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def _gh_get(path: str) -> Optional[Dict]:
    url = f"{_GH_API}{path}"
    try:
        resp = requests.get(url, headers=_gh_headers(), timeout=10)
        if resp.status_code == 200:
            return resp.json()
        if resp.status_code == 404:
            return None
        if resp.status_code == 403:
            reset = int(resp.headers.get("X-RateLimit-Reset", time.time() + 60))
            wait = max(0, reset - int(time.time())) + 2
            print(f"    GitHub rate limit hit, waiting {wait}s …")
            time.sleep(wait)
            resp2 = requests.get(url, headers=_gh_headers(), timeout=10)
            return resp2.json() if resp2.status_code == 200 else None
    except Exception as e:
        print(f"    GitHub API error for {path}: {e}")
    return None


def _fetch_readme(owner: str, repo: str) -> str:
    """Return decoded README text (up to _README_MAX_CHARS), or empty string."""
    data = _gh_get(f"/repos/{owner}/{repo}/readme")
    if not data:
        return ""
    try:
        content = base64.b64decode(data["content"]).decode("utf-8", errors="replace")
        # Strip markdown images and links, collapse whitespace
        content = re.sub(r"!\[.*?\]\(.*?\)", "", content)
        content = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", content)
        content = re.sub(r"\s+", " ", content).strip()
        return content[:_README_MAX_CHARS]
    except Exception:
        return ""


def _enrich_repo(owner: str, repo: str) -> Optional[Dict]:
    """Call GitHub API to get topics, pushed_at, description, archived flag."""
    return _gh_get(f"/repos/{owner}/{repo}")


# ── Keyword matching (Stage 1) ────────────────────────────────────────────────


def _keyword_match(repo: Dict, keywords: List[str]) -> bool:
    """Return True if at least one keyword appears in searchable repo fields."""
    haystack = " ".join(
        [
            repo.get("name", ""),
            repo.get("description", ""),
            " ".join(repo.get("topics", [])),
        ]
    ).lower()
    return any(kw.lower() in haystack for kw in keywords)


# ── LLM scoring (Stage 2) ─────────────────────────────────────────────────────


def _llm_score(repo: Dict, readme: str, topic_categories: List[str], interests: str) -> Dict:
    """Return {relevance, topic_category, summary, tags} from LLM, or {}."""
    prompt = GITHUB_TRENDING_PROMPT.format(
        name=repo.get("full_name", ""),
        description=repo.get("description", "") or "(none)",
        language=repo.get("language", "") or "unknown",
        topics=", ".join(repo.get("topics", [])) or "(none)",
        stars=repo.get("stargazers_count", 0),
        readme=readme or "(not available)",
        topic_categories=", ".join(topic_categories),
        interests=interests,
    )
    try:
        raw = llm_client.complete(prompt)
        raw = re.sub(r"```json\n?", "", raw)
        raw = re.sub(r"```", "", raw).strip()
        return json.loads(raw)
    except Exception as e:
        print(f"    LLM failed for {repo.get('full_name', '')}: {e}")
        return {}


# ── Main pipeline ─────────────────────────────────────────────────────────────


def run(config: dict) -> List[Dict]:
    """Execute the GitHub Trending pipeline and return saved items."""
    gh_cfg = config.get("github_trending", {})
    if not gh_cfg.get("enabled", False):
        return []

    languages: List[str] = gh_cfg.get("languages", [""])
    since: str = gh_cfg.get("since", "daily")
    relevance_cutoff: int = gh_cfg.get("relevance_cutoff", 3)
    max_repos: int = gh_cfg.get("max_repos", 20)
    topic_categories: List[str] = config.get("topic_categories", [])

    # Build keyword list from arxiv topic_interests + interests string
    # + github_trending-specific keywords
    arxiv_cfg = config.get("arxiv", {})
    interest_keywords: List[str] = list(arxiv_cfg.get("topic_interests", []))
    raw_interests: str = arxiv_cfg.get("interests", "")
    for kw in re.split(r"[,\n]+", raw_interests):
        kw = kw.strip()
        if kw:
            interest_keywords.append(kw)
    # Merge GitHub-specific keywords from config
    interest_keywords.extend(gh_cfg.get("keywords", []))
    # Deduplicate, preserve order
    seen: set = set()
    keywords: List[str] = []
    for kw in interest_keywords:
        if kw.lower() not in seen:
            seen.add(kw.lower())
            keywords.append(kw)

    interests_text = ", ".join(keywords)

    try:
        import gtrending  # type: ignore
    except ImportError:
        print("  gtrending not installed — skipping GitHub Trending pipeline")
        return []

    # ── Step 1: Fetch from gtrending ──────────────────────────────────────────
    raw_repos: List[Dict] = []
    for lang in languages:
        try:
            fetched = gtrending.fetch_repos(since=since, language=lang or "")
            print(f"  gtrending [{lang or 'all'}]: {len(fetched)} repos")
            raw_repos.extend(fetched)
        except Exception as e:
            print(f"  gtrending fetch failed for lang={lang!r}: {e}")

    if not raw_repos:
        return []

    # Deduplicate by (author, name)
    seen_repos: set = set()
    unique_repos: List[Dict] = []
    for r in raw_repos:
        key = (r.get("author", ""), r.get("name", ""))
        if key not in seen_repos:
            seen_repos.add(key)
            unique_repos.append(r)

    print(f"  {len(unique_repos)} unique repos after dedup")

    # ── Step 2 & 3: GitHub API enrichment + filter archived ───────────────────
    # Use GitHub API if token is available. If the API call fails (expired token,
    # 401, rate limit, network error), fall back to gtrending data rather than
    # dropping the repo. Only skip a repo when it's explicitly marked archived.
    use_api = bool(os.environ.get("GITHUB_TOKEN", "").strip())
    api_ok_count = 0
    enriched: List[Dict] = []
    for r in unique_repos:
        owner = r.get("author", "")
        repo_name = r.get("name", "")
        if not owner or not repo_name:
            continue

        api_data = _enrich_repo(owner, repo_name) if use_api else None

        if api_data is not None:
            if api_data.get("archived", False):
                continue  # filter archived repos
            r["full_name"] = api_data.get("full_name", f"{owner}/{repo_name}")
            r["description"] = api_data.get("description") or r.get("description", "") or ""
            r["topics"] = api_data.get("topics", [])
            r["pushed_at"] = api_data.get("pushed_at", "")
            r["stargazers_count"] = api_data.get("stargazers_count", r.get("stars", 0))
            r["language"] = api_data.get("language") or r.get("language", "")
            r["html_url"] = api_data.get("html_url", f"https://github.com/{owner}/{repo_name}")
            api_ok_count += 1
        else:
            # API unavailable / failed — use gtrending data directly
            r["full_name"] = f"{owner}/{repo_name}"
            r["description"] = r.get("description", "") or ""
            r["topics"] = []
            r["pushed_at"] = ""
            r["stargazers_count"] = r.get("stars", 0)
            r["language"] = r.get("language", "")
            r["html_url"] = r.get("url", f"https://github.com/{owner}/{repo_name}")

        enriched.append(r)

    if use_api and api_ok_count == 0:
        print("  Warning: GITHUB_TOKEN set but all API calls failed (expired/invalid?)")
    mode_note = f"with API ({api_ok_count} enriched)" if use_api else "from gtrending (no token)"
    print(f"  {len(enriched)} repos normalised {mode_note}")

    # ── Step 4: Stage 1 – keyword match ───────────────────────────────────────
    matched: List[Dict] = [r for r in enriched if _keyword_match(r, keywords)]
    print(f"  {len(matched)} repos passed Stage 1 keyword match")
    if not matched:
        return []

    # Cap before LLM calls
    matched = matched[:max_repos]

    # ── Step 5: Dedup against DB ──────────────────────────────────────────────
    new_repos = [r for r in matched if not database.news_exists(r["html_url"])]
    print(f"  {len(new_repos)} repos not yet in DB")
    if not new_repos:
        return []

    # ── Step 6: Stage 2 – LLM scoring, with README fallback ──────────────────
    results: List[Dict] = []
    today = date.today().isoformat()

    for r in new_repos:
        owner_name = r["full_name"].split("/")[0] if "/" in r["full_name"] else r.get("author", "")
        repo_name = r["full_name"].split("/")[1] if "/" in r["full_name"] else r.get("name", "")

        # Fetch README when description is thin (< 80 chars or no topics)
        readme = ""
        if len(r.get("description", "")) < 80 or not r.get("topics"):
            readme = _fetch_readme(owner_name, repo_name)

        print(f"  Scoring: {r['full_name']} …")
        analysis = _llm_score(r, readme, topic_categories, interests_text)
        if not analysis:
            continue

        relevance = int(analysis.get("relevance", 1))
        if relevance < relevance_cutoff:
            continue

        # Format pushed_at as YYYY-MM-DD
        pushed_raw = r.get("pushed_at", "") or ""
        published_date = pushed_raw[:10] if pushed_raw else today

        item: Dict = {
            "url": r["html_url"],
            "title": r["full_name"],
            "source": "GitHub Trending",
            "summary": analysis.get("summary", ""),
            "tags": analysis.get("tags", ""),
            "topic_category": analysis.get("topic_category", ""),
            "relevance": relevance,
            "published_date": published_date,
        }
        results.append(item)

    # ── Step 7: Sort by pushed_at descending ──────────────────────────────────
    results.sort(key=lambda x: x.get("published_date", ""), reverse=True)

    # ── Step 8: Write to DB ───────────────────────────────────────────────────
    for item in results:
        database.upsert_news_item(item)
    print(f"  Saved {len(results)} GitHub Trending repos to database")

    return results
