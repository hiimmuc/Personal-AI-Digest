"""News pipeline: fetch RSS feeds → dedup → LLM summarize+score → DB."""

import json
import re
from datetime import datetime, timezone
from typing import Dict, List

import feedparser

from ..db import database
from ..llm import client as llm_client
from ..llm.prompts import NEWS_PROMPT


def fetch_rss_feed(source: Dict, since: datetime) -> List[Dict]:
    """Fetch items from a single RSS feed published after `since`."""
    items = []
    try:
        feed = feedparser.parse(source["url"])
        for entry in feed.entries:
            pub = entry.get("published_parsed") or entry.get("updated_parsed")
            if pub:
                pub_dt = datetime(*pub[:6], tzinfo=timezone.utc)
                if pub_dt < since:
                    continue

            url = entry.get("link", "")
            if not url:
                continue

            # Extract text content, strip HTML
            raw_content = entry.get("summary", "")
            if not raw_content and entry.get("content"):
                raw_content = entry["content"][0].get("value", "")
            content = re.sub("<[^<]+?>", "", raw_content).strip()

            items.append(
                {
                    "url": url,
                    "title": entry.get("title", ""),
                    "source": source["name"],
                    "content": content[:2000],
                    "published_date": entry.get("published", "")[:10],
                }
            )
    except Exception as e:
        print(f"  RSS fetch failed for '{source['name']}': {e}")
    return items


def summarize_and_score(item: Dict, topic_categories: List[str]) -> Dict:
    """Call LLM to summarize and score one news item."""
    prompt = NEWS_PROMPT.format(
        source=item["source"],
        title=item["title"],
        content=item.get("content", ""),
        topic_categories=", ".join(topic_categories),
        url=item["url"],
    )
    try:
        raw = llm_client.complete(prompt)
        raw = re.sub(r"```json\n?", "", raw)
        raw = re.sub(r"```", "", raw).strip()
        return json.loads(raw)
    except Exception as e:
        print(f"  LLM failed for '{item['title'][:50]}': {e}")
        return {}


def run(config: dict, since: datetime) -> List[Dict]:
    """Execute the full news pipeline and return saved items."""
    news_cfg = config["news"]
    relevance_cutoff: int = news_cfg.get("relevance_cutoff", 2)
    topic_categories: List[str] = config["topic_categories"]
    sources = [s for s in news_cfg.get("sources", []) if s.get("enabled", True)]

    # 1. Fetch from all enabled sources
    all_items: List[Dict] = []
    for source in sources:
        items = fetch_rss_feed(source, since)
        print(f"  {source['name']}: {len(items)} items")
        all_items.extend(items)
    print(f"Fetched {len(all_items)} news items total")

    # 2. Deduplicate by URL against SQLite
    new_items = [i for i in all_items if not database.news_exists(i["url"])]
    print(f"{len(new_items)} new items (not in DB)")
    if not new_items:
        return []

    # 3. LLM: summarize + score each item, filter below cutoff
    results: List[Dict] = []
    for item in new_items:
        print(f"  Analyzing: {item['title'][:60]}...")
        analysis = summarize_and_score(item, topic_categories)
        if not analysis:
            continue
        relevance = int(analysis.get("relevance", 1))
        if relevance < relevance_cutoff:
            continue
        item.update(
            {
                "summary": analysis.get("summary", ""),
                "tags": analysis.get("tags", ""),
                "topic_category": analysis.get("topic_category", ""),
                "relevance": relevance,
            }
        )
        results.append(item)

    # 4. Write to SQLite
    for item in results:
        database.upsert_news_item(item)
    print(f"Saved {len(results)} news items to database")

    return results
