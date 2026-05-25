"""Outbound Telegram push — daily and weekly digests (V1: send only)."""

import os

import requests


def _send(text: str) -> None:
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    resp = requests.post(
        url,
        json={"chat_id": chat_id, "text": text, "parse_mode": "Markdown"},
        timeout=15,
    )
    resp.raise_for_status()


def push_daily(papers: list, news_items: list, digest_date: str) -> None:
    """Send daily digest summary to Telegram."""
    lines = [f"*AI Digest — {digest_date}*", ""]

    if papers:
        lines.append("*Research Papers:*")
        for i, p in enumerate(papers, 1):
            lines.append(f"{i}. [{p['title']}](https://arxiv.org/abs/{p['arxiv_id']})")
        lines.append("")

    if news_items:
        lines.append("*Tech News:*")
        for i, n in enumerate(news_items, 1):
            lines.append(f"{i}. [{n['title']}]({n['url']}) — _{n.get('source', '')}_")

    _send("\n".join(lines))


def push_weekly(papers: list, news_items: list, week: int, narrative: str) -> None:
    """Send weekly rollup summary to Telegram."""
    lines = [
        f"*AI Digest — Week {week} Rollup*",
        "",
        f"_{narrative}_",
        "",
    ]

    if papers:
        lines.append("*Top Papers:*")
        for i, p in enumerate(papers[:5], 1):
            lines.append(f"{i}. [{p['title']}](https://arxiv.org/abs/{p['arxiv_id']})")
        lines.append("")

    if news_items:
        lines.append("*Top News:*")
        for i, n in enumerate(news_items[:5], 1):
            lines.append(f"{i}. [{n['title']}]({n['url']})")

    _send("\n".join(lines))
