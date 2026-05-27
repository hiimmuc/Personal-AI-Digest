"""News pipeline: fetch RSS feeds -> dedup -> LLM summarize+score -> DB."""

import logging
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from typing import Dict, List

import feedparser
from tqdm import tqdm

from ..db import database
from ..llm import client as llm_client
from ..llm.prompts import NEWS_PROMPT
from ..llm.scoring import parse_json_response

logger = logging.getLogger(__name__)

MAX_WORKERS = 4


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
            raw = entry.get("summary", "")
            if not raw and entry.get("content"):
                raw = entry["content"][0].get("value", "")
            items.append({
                "url": url,
                "title": entry.get("title", ""),
                "source": source["name"],
                "content": re.sub("<[^<]+?>", "", raw).strip()[:2000],
                "published_date": entry.get("published", "")[:10],
            })
    except Exception as e:
        logger.warning("RSS fetch failed for '%s': %s", source["name"], e)
    return items


def _analyze_item(item: Dict, topic_categories: List[str]) -> Dict:
    """Call LLM to summarize and score one news item. Returns analysis dict or {}."""
    prompt = NEWS_PROMPT.format(
        source=item["source"],
        title=item["title"],
        content=item.get("content", ""),
        topic_categories=", ".join(topic_categories),
        url=item["url"],
    )
    try:
        return parse_json_response(llm_client.complete(prompt))
    except Exception as e:
        logger.warning("LLM failed for '%s': %s", item["title"][:60], e)
        return {}


def run(config: dict, since: datetime) -> List[Dict]:
    """Execute the full news pipeline and return saved items."""
    news_cfg = config["news"]
    relevance_cutoff: int = news_cfg.get("relevance_cutoff", 2)
    topic_categories: List[str] = config["topic_categories"]
    sources = [s for s in news_cfg.get("sources", []) if s.get("enabled", True)]

    # 1. Fetch all enabled sources
    all_items: List[Dict] = []
    for source in sources:
        items = fetch_rss_feed(source, since)
        logger.info("%s: %d items", source["name"], len(items))
        all_items.extend(items)
    logger.info("Fetched %d news items total", len(all_items))

    # 2. Deduplicate by URL against DB
    new_items = [i for i in all_items if not database.news_exists(i["url"])]
    logger.info("%d new items (not in DB)", len(new_items))
    if not new_items:
        return []

    # 3. LLM: analyze all items concurrently, filter below cutoff
    llm_client.try_init()
    results: List[Dict] = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {pool.submit(_analyze_item, item, topic_categories): item for item in new_items}
        for future in tqdm(as_completed(futures), total=len(new_items), desc="Analyzing news"):
            item = futures[future]
            try:
                analysis = future.result()
            except Exception as e:
                logger.warning("Analysis failed: %s", e)
                continue
            if not analysis:
                continue
            relevance = int(analysis.get("relevance", 1))
            if relevance < relevance_cutoff:
                continue
            item.update({
                "summary": analysis.get("summary", ""),
                "tags": analysis.get("tags", ""),
                "topic_category": analysis.get("topic_category", ""),
                "relevance": relevance,
            })
            results.append(item)

    # 4. Write to DB
    for item in results:
        database.upsert_news_item(item)
    logger.info("Saved %d news items to database", len(results))
    return results
