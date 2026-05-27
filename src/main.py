"""Daily pipeline entrypoint: ArXiv + News -> SQLite -> Markdown."""

import logging
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import yaml
from dotenv import load_dotenv

from .db import database
from .llm import client as llm_client
from .llm.prompts import DIGEST_SUMMARY_PROMPT
from .pipelines import arxiv_pipeline, github_trending_pipeline, news_pipeline
from .render import daily as daily_renderer

load_dotenv()  # populate env vars from .env before any config is read
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

_SITE_DIR = Path(__file__).parent.parent / "site" / "_posts"
_SITE_DATA = Path(__file__).parent.parent / "site" / "_data"


def _load_config() -> dict:
    path = Path(__file__).parent / "configs" / "config.yaml"
    with open(path) as f:
        return yaml.safe_load(f)


def _write_jekyll_data(config: dict) -> None:
    """Write site/_data/arxiv_config.yml so the sidebar template can read it."""
    from .render.daily import ARXIV_SUBJECTS

    arxiv_cfg = config.get("arxiv", {})
    categories = [
        {
            "code": cat,
            "name": ARXIV_SUBJECTS.get(cat, cat),
        }
        for cat in arxiv_cfg.get("categories", [])
    ]
    topic_interests = arxiv_cfg.get("topic_interests", [])

    _SITE_DATA.mkdir(parents=True, exist_ok=True)
    data_path = _SITE_DATA / "arxiv_config.yml"
    with open(data_path, "w", encoding="utf-8") as f:
        yaml.dump(
            {"categories": categories, "topic_interests": topic_interests},
            f,
            default_flow_style=False,
            allow_unicode=True,
        )
    logger.info("Wrote Jekyll data -> %s", data_path)


def _digest_summary(papers: list, news: list) -> str:
    paper_titles = [f"[paper] {p['title']}" for p in papers[:15]]
    news_titles = [f"[news] {n['title']}" for n in news[:10]]
    titles = paper_titles + news_titles
    if not titles:
        return ""
    prompt = DIGEST_SUMMARY_PROMPT.format(items="\n".join(f"- {t}" for t in titles))
    try:
        return llm_client.complete(prompt).strip()
    except Exception as e:
        logger.warning("Digest summary failed: %s", e)
        return ""


def main() -> None:
    config = _load_config()
    database.init_db()
    _write_jekyll_data(config)

    today = date.today().isoformat()
    since = datetime.now(timezone.utc) - timedelta(hours=26)

    logger.info("=== Daily Digest: %s ===", today)

    logger.info("--- ArXiv Pipeline ---")
    arxiv_pipeline.run(config)

    # Read today's papers from DB sorted by relevance, capped at max_papers_per_day
    arxiv_cfg = config.get("arxiv", {})
    gh_cfg = config.get("github_trending", {})
    max_papers = arxiv_cfg.get("max_papers_per_day", 20)
    gh_cutoff = gh_cfg.get("relevance_cutoff", 3)
    max_gh = gh_cfg.get("max_repos", 15)

    papers = sorted(
        database.get_papers_for_date(today) or [],
        key=lambda p: p.get("relevance", 0),
        reverse=True,
    )[:max_papers]

    print("\n--- News Pipeline ---")
    # Use pipeline return value (only newly discovered items for today)
    news_items = news_pipeline.run(config, since) or []

    print("\n--- GitHub Trending Pipeline ---")
    github_trending_pipeline.run(config)

    # Read GitHub trending from DB — handles re-runs where repos were already
    # saved in a previous run (pipeline returns [] when nothing is new)
    gh_items = sorted(
        [
            n
            for n in (database.get_news_for_date(today) or [])
            if n.get("source", "") == "GitHub Trending" and n.get("relevance", 0) >= gh_cutoff
        ],
        key=lambda n: n.get("relevance", 0),
        reverse=True,
    )[:max_gh]
    news_items = news_items + gh_items

    theme = _digest_summary(papers, news_items)

    content = daily_renderer.render_daily(papers, news_items, today, theme)

    # Write Jekyll post: site/_posts/YYYY-MM-DD-daily.md
    _SITE_DIR.mkdir(parents=True, exist_ok=True)
    post_path = _SITE_DIR / f"{today}-daily.md"
    post_path.write_text(content, encoding="utf-8")
    print(f"\nWrote digest → {post_path}")


if __name__ == "__main__":
    main()
