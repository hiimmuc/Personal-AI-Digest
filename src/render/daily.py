"""Render daily digest Markdown for GitHub Pages (Jekyll)."""

import json
from collections import defaultdict
from typing import Dict, List

_DOTS = {1: "●○○○○", 2: "●●○○○", 3: "●●●○○", 4: "●●●●○", 5: "●●●●●"}


def _dots(score: int) -> str:
    return _DOTS.get(score, "○○○○○")


def render_paper(paper: Dict) -> str:
    insights = paper.get("insights") or {}
    if isinstance(insights, str):
        try:
            insights = json.loads(insights)
        except Exception:
            insights = {}

    arxiv_id = paper["arxiv_id"]
    code_url = paper.get("code_url", "")
    code_badge = (
        f" &nbsp;[![Code on GitHub](https://img.shields.io/badge/Code-GitHub-black?logo=github&style=flat-square)]({code_url})"
        if code_url
        else ""
    )
    lines = [
        '<div class="paper-item">',
        "",
        f'**[R: {_dots(paper.get("relevance", 0))}]**{code_badge} '
        f'`{paper.get("categories", "")}` &nbsp;·&nbsp; {paper.get("published_date", "")}',
        "",
        f'#### [{paper["title"]}](https://arxiv.org/abs/{arxiv_id})',
        "",
        f'Authors: {paper.get("authors", "")} &nbsp;·&nbsp; '
        f"[arxiv.org/abs/{arxiv_id}](https://arxiv.org/abs/{arxiv_id})",
        "",
    ]

    if paper.get("abstract"):
        lines += [
            "<details>",
            "<summary>Abstract</summary>",
            "",
            paper["abstract"],
            "",
            "</details>",
            "",
        ]

    if insights:
        lines += ["<details>", "<summary>Insights</summary>", ""]
        for key, label in [
            ("contribution", "Contribution"),
            ("core_idea", "Core Idea"),
            ("technique", "Technique"),
            ("pipeline", "Pipeline"),
            ("methodology", "Methodology"),
            ("results", "Results"),
            ("limitations", "Limitations"),
        ]:
            if insights.get(key):
                lines += [f"**{label}:** {insights[key]}", ""]
        lines += ["</details>", ""]

    lines += ["</div>", "", "---", ""]
    return "\n".join(lines)


def render_news_item(item: Dict) -> str:
    tags = " · ".join(f"`{t.strip()}`" for t in item.get("tags", "").split(",") if t.strip())
    lines = [
        '<div class="news-item">',
        "",
        f'**[{item.get("source", "")}]** &nbsp;{item.get("published_date", "")}',
        "",
        f'#### [{item["title"]}]({item["url"]})',
        "",
        item.get("summary", ""),
        "",
        tags,
        "",
        "</div>",
        "",
        "---",
        "",
    ]
    return "\n".join(lines)


def render_daily(
    papers: List[Dict],
    news_items: List[Dict],
    digest_date: str,
    theme_sentence: str = "",
) -> str:
    """Render a full daily digest Markdown page."""
    papers_by_topic: Dict[str, List] = defaultdict(list)
    for p in papers:
        papers_by_topic[p.get("topic_category") or "General"].append(p)

    news_by_topic: Dict[str, List] = defaultdict(list)
    for n in news_items:
        news_by_topic[n.get("topic_category") or "General"].append(n)

    lines = [
        "---",
        "layout: default",
        f'title: "Daily Digest {digest_date}"',
        f"date: {digest_date}",
        f"permalink: /digest/{digest_date}/",
        "---",
        "",
        f"# {digest_date}",
        "",
    ]

    if theme_sentence:
        lines += [f"*{theme_sentence}*", ""]

    lines += [
        "<hr>",
        "",
        '[Sort: Most Recent](#recent "sort=recent") · '
        '[Sort: Most Relevant](#relevant "sort=relevance")',
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
