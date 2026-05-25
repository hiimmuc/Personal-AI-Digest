"""Daily pipeline entrypoint: ArXiv + News → SQLite → Markdown → Telegram."""

from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import yaml
from dotenv import load_dotenv

load_dotenv()

from .db import database
from .delivery import telegram
from .llm import client as llm_client
from .llm.prompts import THEME_SENTENCE_PROMPT
from .pipelines import arxiv_pipeline, news_pipeline
from .render import daily as daily_renderer

_SITE_DIR = Path(__file__).parent.parent / "site" / "_posts"


def _load_config() -> dict:
    path = Path(__file__).parent / "configs" / "config.yaml"
    with open(path) as f:
        return yaml.safe_load(f)


def _theme_sentence(papers: list, news: list) -> str:
    titles = [p["title"] for p in papers[:5]] + [n["title"] for n in news[:5]]
    if not titles:
        return ""
    prompt = THEME_SENTENCE_PROMPT.format(items="\n".join(f"- {t}" for t in titles))
    try:
        return llm_client.complete(prompt).strip()
    except Exception as e:
        print(f"Theme sentence failed: {e}")
        return ""


def main() -> None:
    config = _load_config()
    database.init_db()

    today = date.today().isoformat()
    since = datetime.now(timezone.utc) - timedelta(hours=26)

    print(f"=== Daily Digest: {today} ===\n")

    print("--- ArXiv Pipeline ---")
    papers = arxiv_pipeline.run(config) or []

    print("\n--- News Pipeline ---")
    news_items = news_pipeline.run(config, since) or []

    theme = _theme_sentence(papers, news_items)

    content = daily_renderer.render_daily(papers, news_items, today, theme)

    # Write Jekyll post: site/_posts/YYYY-MM-DD-daily.md
    _SITE_DIR.mkdir(parents=True, exist_ok=True)
    post_path = _SITE_DIR / f"{today}-daily.md"
    post_path.write_text(content, encoding="utf-8")
    print(f"\nWrote digest → {post_path}")

    if config.get("delivery", {}).get("telegram_enabled", False):
        try:
            telegram.push_daily(papers, news_items, today)
            print("Telegram push sent")
        except Exception as e:
            print(f"Telegram push failed: {e}")


if __name__ == "__main__":
    main()
