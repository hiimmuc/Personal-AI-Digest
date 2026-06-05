"""Render weekly rollup Markdown for GitHub Pages (Jekyll)."""

import html as _html
import json
import re
from collections import defaultdict
from typing import Dict, List

from .daily import _format_date, _render_subject_tags, render_news_item

TOP_N = 10


def _compact_paper(paper: Dict, rank: int) -> str:
    arxiv_id = paper["arxiv_id"]
    relevance = paper.get("relevance", 0)
    filled = relevance if 1 <= relevance <= 5 else 0

    insights = paper.get("insights") or {}
    if isinstance(insights, str):
        try:
            insights = json.loads(insights)
        except Exception:
            insights = {}
    contribution = (insights.get("contribution") or insights.get("core_idea") or "").strip()

    cat_tags = _render_subject_tags(paper.get("categories", ""))
    date_str = _format_date(paper.get("published_date", ""), arxiv_id)

    rel_html = (
        '<span class="rel-dots" aria-label="Relevance: '
        + str(filled)
        + ' out of 5">'
        + '<span class="rel-dot filled"></span>' * filled
        + '<span class="rel-dot"></span>' * (5 - filled)
        + "</span>"
    )

    contribution_html = (
        f'<p class="weekly-paper-contribution">{_html.escape(contribution)}</p>'
        if contribution
        else ""
    )

    return f"""\
<div class="weekly-paper-item">
  <div class="weekly-paper-header">
    <span class="weekly-rank">#{rank}</span>
    {rel_html}
    {cat_tags}
    <span class="paper-date">{date_str}</span>
  </div>
  <a class="paper-title" href="https://arxiv.org/abs/{arxiv_id}">{_html.escape(paper["title"])}</a>
  {contribution_html}
</div>
"""


def _compact_repo(repo: Dict, rank: int) -> str:
    url = repo.get("url", "#")
    full_name = repo.get("title", "")
    summary = _html.escape(repo.get("summary", ""))
    stars = repo.get("stars", 0) or 0
    topic_category = _html.escape(repo.get("topic_category", ""))

    if "/" in full_name:
        owner, repo_name = full_name.split("/", 1)
    else:
        owner, repo_name = "", full_name

    raw_tags = [t.strip() for t in repo.get("tags", "").split(",") if t.strip()]
    tag_html = "".join(
        f'<span class="gh-tag">{_html.escape(t)}</span>' for t in raw_tags[:4]
    )

    if stars >= 1000:
        stars_str = f"{stars / 1000:.1f}k"
    else:
        stars_str = str(stars)

    topic_pill = (
        f'<span class="gh-topic-pill">{topic_category}</span>' if topic_category else ""
    )

    return f"""\
<div class="weekly-repo-item">
  <div class="weekly-repo-header">
    <span class="weekly-rank">#{rank}</span>
    <a class="gh-repo-link" href="{url}" target="_blank" rel="noopener noreferrer">
      <span class="gh-owner">{_html.escape(owner)}</span><span class="gh-sep">/</span><strong class="gh-repo">{_html.escape(repo_name)}</strong>
    </a>
    {topic_pill}
    <span class="weekly-stars">&#9733; {stars_str}</span>
  </div>
  <p class="gh-summary">{summary}</p>
  <div class="gh-tags">{tag_html}</div>
</div>
"""


def render_weekly(
    papers: List[Dict],
    news_items: List[Dict],
    repos: List[Dict],
    week: int,
    date_range: str,
    narrative: str,
) -> str:
    """Render a weekly rollup Markdown page."""
    topic_papers = [p for p in papers if p.get("discovery_type") == "topic"]
    subject_papers = [p for p in papers if p.get("discovery_type", "subject") != "topic"]

    interest_groups: Dict[str, List] = defaultdict(list)
    for p in topic_papers:
        interest_groups[p.get("search_topic") or "General"].append(p)

    subject_groups: Dict[str, List] = defaultdict(list)
    for p in subject_papers:
        subject_groups[p.get("topic_category") or "General"].append(p)

    news_sorted = sorted(news_items, key=lambda x: x.get("relevance", 0), reverse=True)
    repos_sorted = sorted(repos, key=lambda x: (x.get("stars", 0) or 0), reverse=True)

    paper_count = len(papers)
    news_count = len(news_items)
    repo_count = len(repos)

    clean_narrative = re.sub(r"<think>.*?</think>", "", narrative, flags=re.DOTALL).strip()

    lines = [
        "---",
        "layout: modern",
        f'title: "Week {week} — {date_range}"',
        f"week: {week}",
        f"paper_count: {paper_count}",
        f"news_count: {news_count}",
        f"repo_count: {repo_count}",
        f"permalink: /weekly/{week}/",
        "---",
        "",
        # Stats bar
        '<div class="weekly-stats-bar">',
        f'  <span class="weekly-stat"><strong>{paper_count}</strong> papers</span>',
        '  <span class="weekly-stat-sep">·</span>',
        f'  <span class="weekly-stat"><strong>{news_count}</strong> news</span>',
        '  <span class="weekly-stat-sep">·</span>',
        f'  <span class="weekly-stat"><strong>{repo_count}</strong> repos</span>',
        '  <span class="weekly-stat-sep">·</span>',
        f'  <span class="weekly-stat">Week <strong>{week}</strong></span>',
        "</div>",
        "",
        # Narrative callout
        '<div class="weekly-narrative">',
        f"  <p>{_html.escape(clean_narrative)}</p>",
        "</div>",
        "",
        "<hr>",
        "",
    ]

    # ── Research Highlights ──────────────────────────────────────────────────
    if interest_groups or subject_groups:
        lines += ['<h2 id="papers">Research Highlights</h2>', ""]

    if interest_groups:
        lines += [
            '<h3 id="papers-by-interest">By Personal Interest</h3>',
            '<p class="section-desc">Top papers per interest topic, ranked by relevance.</p>',
            "",
        ]
        for interest in sorted(interest_groups):
            group = sorted(
                interest_groups[interest], key=lambda p: p.get("relevance", 0), reverse=True
            )[:TOP_N]
            if not group:
                continue
            lines += [
                f"<h4>{_html.escape(interest)}</h4>",
                '<div class="weekly-paper-list">',
                "",
            ]
            for i, p in enumerate(group, 1):
                lines.append(_compact_paper(p, i))
            lines += ["</div>", ""]

    if subject_groups:
        lines += [
            '<h3 id="papers-by-area">By Research Area</h3>',
            '<p class="section-desc">Top papers per ArXiv subject category, ranked by relevance.</p>',
            "",
        ]
        for area in sorted(subject_groups):
            group = sorted(
                subject_groups[area], key=lambda p: p.get("relevance", 0), reverse=True
            )[:TOP_N]
            if not group:
                continue
            lines += [
                f"<h4>{_html.escape(area)}</h4>",
                '<div class="weekly-paper-list">',
                "",
            ]
            for i, p in enumerate(group, 1):
                lines.append(_compact_paper(p, i))
            lines += ["</div>", ""]

    # ── Top News ─────────────────────────────────────────────────────────────
    if news_sorted:
        lines += ['<h2 id="news">Top News</h2>', ""]
        for n in news_sorted[:TOP_N]:
            lines.append(render_news_item(n))
        lines.append("")

    # ── Trending Repos ────────────────────────────────────────────────────────
    if repos_sorted:
        lines += [
            '<h2 id="repos">Trending Repos</h2>',
            '<p class="section-desc">Top repositories this week, sorted by stars.</p>',
            "",
            '<div class="weekly-repo-list">',
            "",
        ]
        for i, r in enumerate(repos_sorted[:TOP_N], 1):
            lines.append(_compact_repo(r, i))
        lines += ["</div>", ""]

    return "\n".join(lines)
