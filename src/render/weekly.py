"""Render weekly rollup Markdown for GitHub Pages (Jekyll)."""

from collections import defaultdict
from typing import Dict, List

from .daily import render_news_item, render_paper


def render_weekly(
    papers: List[Dict],
    news_items: List[Dict],
    week: int,
    date_range: str,
    narrative: str,
) -> str:
    """Render a weekly rollup Markdown page."""
    papers_by_topic: Dict[str, List] = defaultdict(list)
    for p in papers:
        papers_by_topic[p.get("topic_category") or "General"].append(p)

    news_by_topic: Dict[str, List] = defaultdict(list)
    for n in news_items:
        news_by_topic[n.get("topic_category") or "General"].append(n)

    lines = [
        "---",
        "layout: default",
        f'title: "Week {week} Rollup ({date_range})"',
        f"permalink: /weekly/{week}/",
        "---",
        "",
        f"# Week {week} — {date_range}",
        "",
        f"> {narrative}",
        "",
        "<hr>",
        "",
    ]

    if papers:
        lines += ["## Research Papers", ""]
        for topic in sorted(papers_by_topic):
            lines += [f"### {topic}", ""]
            for p in papers_by_topic[topic]:
                lines.append(render_paper(p))

    if news_items:
        lines += ["## Tech News", ""]
        for topic in sorted(news_by_topic):
            lines += [f"### {topic}", ""]
            for n in news_by_topic[topic]:
                lines.append(render_news_item(n))

    return "\n".join(lines)
