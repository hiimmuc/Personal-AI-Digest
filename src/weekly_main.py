"""Weekly rollup entrypoint: query DB → LLM narrative → Markdown → Telegram."""

from datetime import date, timedelta
from pathlib import Path

import yaml
from dotenv import load_dotenv

load_dotenv()

from .db import database
from .delivery import telegram
from .llm import client as llm_client
from .llm.prompts import WEEKLY_NARRATIVE_PROMPT
from .render import weekly as weekly_renderer

_SITE_DIR = Path(__file__).parent.parent / "site" / "_weekly"


def _load_config() -> dict:
    path = Path(__file__).parent / "configs" / "config.yaml"
    with open(path) as f:
        return yaml.safe_load(f)


def _narrative(papers: list, news: list) -> str:
    papers_text = "\n".join(f"- {p['title']}" for p in papers[:10])
    news_text = "\n".join(f"- {n['title']}" for n in news[:10])
    prompt = WEEKLY_NARRATIVE_PROMPT.format(papers=papers_text, news=news_text)
    try:
        return llm_client.complete(prompt).strip()
    except Exception as e:
        print(f"Narrative generation failed: {e}")
        return "This week in AI and tech."


def main() -> None:
    config = _load_config()

    today = date.today()
    week = today.isocalendar()[1]
    monday = today - timedelta(days=today.weekday())
    sunday = monday + timedelta(days=6)
    date_range = f"{monday.isoformat()} – {sunday.isoformat()}"

    print(f"=== Weekly Rollup: Week {week} ({date_range}) ===\n")

    papers = database.get_papers_for_week(week)
    news_items = database.get_news_for_week(week)
    print(f"Found {len(papers)} papers, {len(news_items)} news items for week {week}")

    narrative = _narrative(papers, news_items)

    content = weekly_renderer.render_weekly(papers, news_items, week, date_range, narrative)

    _SITE_DIR.mkdir(parents=True, exist_ok=True)
    out_path = _SITE_DIR / f"week-{week:02d}.md"
    out_path.write_text(content, encoding="utf-8")
    print(f"Wrote weekly rollup → {out_path}")

    if config.get("delivery", {}).get("telegram_enabled", False):
        try:
            telegram.push_weekly(papers, news_items, week, narrative)
            print("Telegram push sent")
        except Exception as e:
            print(f"Telegram push failed: {e}")


if __name__ == "__main__":
    main()
