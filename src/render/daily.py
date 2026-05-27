"""Render daily digest Markdown for GitHub Pages (Jekyll)."""

import html as _html
import json
import re
from collections import defaultdict
from datetime import datetime
from typing import Dict, List

_DOTS = {1: "●○○○○", 2: "●●○○○", 3: "●●●○○", 4: "●●●●○", 5: "●●●●●"}

# Human-readable names for ArXiv subject codes
ARXIV_SUBJECTS: Dict[str, str] = {
    "cs.AI": "Artificial Intelligence",
    "cs.CL": "Computation and Language",
    "cs.CV": "Computer Vision and Pattern Recognition",
    "cs.LG": "Machine Learning",
    "cs.RO": "Robotics",
    "cs.LO": "Logic in Computer Science",
    "cs.HC": "Human-Computer Interaction",
    "cs.IR": "Information Retrieval",
    "cs.DC": "Distributed, Parallel, and Cluster Computing",
    "cs.NE": "Neural and Evolutionary Computing",
    "cs.SE": "Software Engineering",
    "cs.CR": "Cryptography and Security",
    "cs.MA": "Multiagent Systems",
    "cs.GT": "Computer Science and Game Theory",
    "cs.SY": "Systems and Control",
    "cs.PL": "Programming Languages",
    "cs.DS": "Data Structures and Algorithms",
    "cs.DB": "Databases",
    "eess.IV": "Image and Video Processing",
    "eess.AS": "Audio and Speech Processing",
    "eess.SP": "Signal Processing",
    "stat.ML": "Machine Learning (Statistics)",
    "math.OC": "Optimization and Control",
    "q-bio.NC": "Neurons and Cognition",
}


def _subject_label(code: str) -> str:
    """Return 'Full Name (cs.XX)' or just the code if unknown."""
    name = ARXIV_SUBJECTS.get(code)
    return f"{name} ({code})" if name else code


def _dots(score: int) -> str:
    return _DOTS.get(score, "○○○○○")


def _format_date(raw: str, arxiv_id: str = "") -> str:
    """Format a published_date value for display.

    Priority:
    1. Parse as YYYY-MM-DD → "D Mon YYYY"  (e.g. "20 May 2026").
    2. If that fails (old truncated RSS format), derive month/year from
       the arXiv ID prefix YYMM  (e.g. '2605' → 'May 2026').
    3. Return raw string as-is.
    """
    if raw:
        try:
            dt = datetime.strptime(raw.strip()[:10], "%Y-%m-%d")
            return f"{dt.day} {dt.strftime('%b %Y')}"  # "20 May 2026"
        except ValueError:
            pass
    # Derive approximate date from arXiv ID: YYMM.NNNNN
    if arxiv_id and len(arxiv_id) >= 4:
        try:
            yy = int(arxiv_id[:2])
            mm = int(arxiv_id[2:4])
            dt = datetime(2000 + yy, mm, 1)
            return dt.strftime("%b %Y")  # "May 2026" (no day available)
        except ValueError:
            pass
    return raw.strip()


def _category_css_class(cat_code: str) -> str:
    """Map a single arXiv category code to a CSS modifier class."""
    cat = (cat_code or "").lower()
    mapping = {
        "cs.ai": "cat-ai",
        "cs.cl": "cat-nlp",
        "cs.cv": "cat-cv",
        "cs.lg": "cat-ml",
        "cs.ro": "cat-ro",
        "cs.hc": "cat-hci",
        "cs.se": "cat-se",
        "cs.ir": "cat-ir",
        "cs.dc": "cat-dc",
        "cs.ne": "cat-ne",
        "cs.cr": "cat-security",
        "cs.ma": "cat-ai",
        "stat.ml": "cat-ml",
        "math.": "cat-math",
        "eess.": "cat-eess",
        "q-bio.": "cat-bio",
        "physics": "cat-physics",
    }
    for prefix, cls in mapping.items():
        if cat.startswith(prefix):
            return cls
    return "cat-default"


def _render_subject_tags(categories_str: str) -> str:
    """Return HTML for one or more category badge spans.

    Each space-separated code becomes a separate badge with its full human-readable
    name, e.g. "Artificial Intelligence (cs.AI)".
    """
    codes = (categories_str or "").split()
    if not codes:
        return ""
    parts = []
    for code in codes:
        css = _category_css_class(code)
        label = _subject_label(code)
        parts.append(f'<span class="cat-tag {css}" title="{label}">{label}</span>')
    return f'<span class="cat-tags">{"".join(parts)}</span>'


def render_paper(paper: Dict) -> str:
    insights = paper.get("insights") or {}
    if isinstance(insights, str):
        try:
            insights = json.loads(insights)
        except Exception:
            insights = {}

    arxiv_id = paper["arxiv_id"]
    code_url = paper.get("code_url", "")
    categories = paper.get("categories", "")
    cat_tags = _render_subject_tags(categories)
    relevance = paper.get("relevance", 0)
    dots = _dots(relevance)

    # ── Action buttons (right column) ─────────────────────────────
    pdf_btn = (
        f'<a class="paper-action-btn pdf-btn" '
        f'href="https://arxiv.org/pdf/{arxiv_id}" '
        f'target="_blank" rel="noopener noreferrer" '
        f'title="Download PDF" aria-label="Download PDF">'
        f'<svg viewBox="0 0 16 16" fill="currentColor" aria-hidden="true">'
        f'<path d="M3.75 1.5a.25.25 0 0 0-.25.25v11.5c0 .138.112.25.25.25h8.5a'
        f".25.25 0 0 0 .25-.25V6H9.75A1.75 1.75 0 0 1 8 4.25V1.5H3.75zm5.75.56"
        f"v2.19c0 .138.112.25.25.25h2.19L9.5 2.06zM2 1.75C2 .784 2.784 0 3.75 0"
        f"h5.086c.464 0 .909.184 1.237.513l3.414 3.414c.329.328.513.773.513 1.237"
        f'V13.25A1.75 1.75 0 0 1 12.25 15h-8.5A1.75 1.75 0 0 1 2 13.25V1.75z"/>'
        f'<path d="M4.5 8.75a.75.75 0 0 1 .75-.75h1a2.25 2.25 0 0 1 0 4.5h-.25V'
        f'13.5a.75.75 0 0 1-1.5 0v-4.75zm1.5.75v1.5h.25a.75.75 0 0 0 0-1.5H6z"'
        f'/><path d="M7.5 8.75a.75.75 0 0 1 .75-.75h1.25a2.25 2.25 0 0 1 0 4.5H'
        f'8.25a.75.75 0 0 1-.75-.75v-3zm1.5.75v2h.5a.75.75 0 0 0 0-1.5H9V9.5z"'
        f'/><path d="M11.25 8a.75.75 0 0 1 .75.75v.75h.5a.75.75 0 0 1 0 1.5H12'
        f'v1.5a.75.75 0 0 1-1.5 0v-3.75A.75.75 0 0 1 11.25 8z"/></svg>'
        f"<span>PDF</span></a>"
    )

    gh_btn = ""
    if code_url:
        gh_btn = (
            f'<a class="paper-action-btn gh-btn" '
            f'href="{code_url}" '
            f'target="_blank" rel="noopener noreferrer" '
            f'title="View code on GitHub" aria-label="View code on GitHub">'
            f'<svg viewBox="0 0 16 16" fill="currentColor" aria-hidden="true">'
            f'<path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07'
            f".55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94"
            f"-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58"
            f" 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2"
            f"-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2"
            f".12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27"
            f" 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27"
            f".82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07"
            f"-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4"
            f'.42-3.58-8-8-8z"/></svg>'
            f"<span>Code</span></a>"
        )

    # ── Relevance dots rendered as filled/empty segments ──────────
    filled = relevance if 1 <= relevance <= 5 else 0
    rel_html = (
        '<span class="rel-dots" aria-label="Relevance: '
        + str(filled)
        + ' out of 5">'
        + '<span class="rel-dot filled"></span>' * filled
        + '<span class="rel-dot"></span>' * (5 - filled)
        + "</span>"
        + f'<span class="rel-score">{filled}/5</span>'
    )

    # ── Body: abstract + insights accordions ──────────────────────
    body_lines = []

    # Strip the arXiv scraper prefix: "arXiv:XXXX Announce Type: new  Abstract: "
    raw_abstract = paper.get("abstract", "")
    clean_abstract = re.sub(
        r"^arXiv:\S+\s+Announce Type:\s*\S+\s+Abstract:\s*",
        "",
        raw_abstract,
        flags=re.IGNORECASE,
    ).strip()

    if clean_abstract:
        body_lines += [
            '<details class="abstract">',
            "<summary>Abstract</summary>",
            f'<p class="paper-detail"><strong>ArXiv ID:</strong>'
            f' <a href="https://arxiv.org/abs/{arxiv_id}" target="_blank"'
            f' rel="noopener noreferrer">{arxiv_id}</a></p>',
            f'<p class="paper-detail"><strong>Authors:</strong>'
            f' {paper.get("authors", "")}</p>',
            '<p class="paper-detail abstract-body">' "<strong>Abstract:</strong></p>",
            f'<p class="abstract-text">{clean_abstract}</p>',
            "</details>",
        ]

    if insights:
        body_lines += ['<details class="insights">', "<summary>Insights</summary>"]
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
                body_lines.append(f"<p><strong>{label}:</strong> {insights[key]}</p>")
        body_lines.append("</details>")

    body_html = "\n".join(body_lines)

    # Derive ISO date for data-date sort attribute
    pub_raw = (paper.get("published_date") or "").strip()
    iso_date = ""
    if re.match(r"\d{4}-\d{2}-\d{2}", pub_raw[:10]):
        iso_date = pub_raw[:10]
    elif len(arxiv_id) >= 4:
        try:
            iso_date = f"20{arxiv_id[:2]}-{arxiv_id[2:4]}-00"
        except Exception:
            pass

    block = f"""\
<div class="paper-item" data-date="{iso_date}" data-relevance="{relevance}">
  <div class="paper-body">
    <div class="paper-meta">
      <span class="relevance-pill">{rel_html}</span>
      {cat_tags}
      <span class="paper-date">{_format_date(paper.get('published_date', ''), arxiv_id)}</span>
    </div>
    <a class="paper-title" href="https://arxiv.org/abs/{arxiv_id}">{paper["title"]}</a>
    <p class="paper-authors">
      <svg class="author-icon" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true" width="12" height="12"><path d="M10.561 8.073a6.005 6.005 0 0 1 3.432 5.142.75.75 0 1 1-1.498.07 4.5 4.5 0 0 0-2.97-3.93l-.04-.012a.75.75 0 0 1 .076-1.27zm-4.5-.31a4.5 4.5 0 0 0-2.97 3.93.75.75 0 0 1-1.498-.07A6.005 6.005 0 0 1 5.025 6.44l-.004.001a.75.75 0 0 1 .04 1.322zM8 7a2 2 0 1 0 0-4 2 2 0 0 0 0 4zm0 1.5a3.5 3.5 0 1 1 0-7 3.5 3.5 0 0 1 0 7z"/></svg>
      {paper.get("authors", "")}
    </p>
{body_html}
  </div>
  <div class="paper-actions">
    {pdf_btn}
    {gh_btn}
  </div>
</div>
"""
    return block


def _news_source_cls(source: str) -> str:
    s = source.lower()
    if "hacker news" in s:
        return "news-source--hn"
    if "reddit" in s:
        return "news-source--reddit"
    if "nvidia" in s:
        return "news-source--nvidia"
    if "hugging face" in s or "huggingface" in s:
        return "news-source--hf"
    return "news-source--default"


def render_news_item(item: Dict) -> str:
    source = item.get("source", "")
    url = item.get("url", "#")
    title = _html.escape(item.get("title", ""))
    summary = _html.escape(item.get("summary", ""))
    date_str = _html.escape(item.get("published_date", ""))
    src_cls = _news_source_cls(source)

    raw_tags = [t.strip() for t in item.get("tags", "").split(",") if t.strip()]
    tag_html = "".join(f'<span class="news-tag">{_html.escape(t)}</span>' for t in raw_tags)

    return f"""\
<div class="news-item">
  <div class="news-meta">
    <span class="news-source {src_cls}">{_html.escape(source)}</span>
    <span class="news-date">{date_str}</span>
  </div>
  <a class="news-title" href="{url}" target="_blank" rel="noopener noreferrer">{title}</a>
  <p class="news-summary">{summary}</p>
  <div class="news-footer">
    <div class="news-tags">{tag_html}</div>
    <a class="news-read-btn" href="{url}" target="_blank" rel="noopener noreferrer">Read&nbsp;more&nbsp;&#8594;</a>
  </div>
</div>
"""


def render_github_trending_item(item: Dict) -> str:
    """Render a single GitHub Trending repo card."""
    url = item.get("url", "#")
    full_name = item.get("title", "")
    summary = _html.escape(item.get("summary", ""))
    date_str = _html.escape(item.get("published_date", ""))
    topic_category = _html.escape(item.get("topic_category", ""))
    relevance = item.get("relevance", 0)

    # Split full_name into owner / repo
    if "/" in full_name:
        owner, repo = full_name.split("/", 1)
    else:
        owner, repo = "", full_name
    owner_esc = _html.escape(owner)
    repo_esc = _html.escape(repo)

    raw_tags = [t.strip() for t in item.get("tags", "").split(",") if t.strip()]
    tag_html = "".join(f'<span class="gh-tag">{_html.escape(t)}</span>' for t in raw_tags[:5])

    filled = max(0, min(5, int(relevance)))
    stars_html = (
        f'<span class="gh-relevance" title="Relevance {filled}/5">'
        + "★" * filled
        + '<span class="gh-relevance-empty">'
        + "★" * (5 - filled)
        + "</span>"
        + f" <span class='gh-rel-num'>{filled}/5</span>"
        + "</span>"
    )

    if topic_category:
        topic_pill = f'<span class="gh-topic-pill">{topic_category}</span>'
    else:
        topic_pill = ""

    return f"""\
<div class="gh-trending-item">
  <div class="gh-trending-header">
    <a class="gh-repo-link" href="{url}" target="_blank" rel="noopener noreferrer">
      <svg class="gh-repo-icon" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true" width="16" height="16"><path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8V1.5Z"/></svg>
      <span class="gh-owner">{owner_esc}</span><span class="gh-sep">/</span><strong class="gh-repo">{repo_esc}</strong>
    </a>
    <div class="gh-trending-badges">
      {topic_pill}
      {stars_html}
    </div>
  </div>
  <p class="gh-summary">{summary}</p>
  <div class="gh-trending-footer">
    <div class="gh-tags">{tag_html}</div>
    <div class="gh-trending-meta">
      <span class="gh-pushed">Updated: {date_str}</span>
      <a class="gh-visit-btn" href="{url}" target="_blank" rel="noopener noreferrer">
        View on GitHub&nbsp;&#8594;
      </a>
    </div>
  </div>
</div>
"""


def render_daily(
    papers: List[Dict],
    news_items: List[Dict],
    digest_date: str,
    theme_sentence: str = "",
) -> str:
    """Render a full daily digest Markdown page."""
    # ── Separate GitHub Trending from regular news ────────────────────────────
    gh_items = [n for n in news_items if n.get("source", "") == "GitHub Trending"]
    regular_news = [n for n in news_items if n.get("source", "") != "GitHub Trending"]

    # Split papers by discovery type
    subject_papers = [p for p in papers if p.get("discovery_type", "subject") != "topic"]
    topic_papers = [p for p in papers if p.get("discovery_type") == "topic"]

    # Group subject papers by LLM-classified topic_category
    subject_by_topic: Dict[str, List] = defaultdict(list)
    for p in subject_papers:
        subject_by_topic[p.get("topic_category") or "General"].append(p)

    # Group topic papers by their search_topic query
    topic_by_interest: Dict[str, List] = defaultdict(list)
    for p in topic_papers:
        topic_by_interest[p.get("search_topic") or "General"].append(p)

    news_by_topic: Dict[str, List] = defaultdict(list)
    for n in regular_news:
        news_by_topic[n.get("topic_category") or "General"].append(n)

    gh_by_topic: Dict[str, List] = defaultdict(list)
    for r in gh_items:
        gh_by_topic[r.get("topic_category") or "General"].append(r)

    # Collect top GitHub trending topic categories for front matter (charts)
    from collections import Counter

    gh_topic_counts: Counter = Counter(r.get("topic_category") or "General" for r in gh_items)
    gh_top_topics = [t for t, _ in gh_topic_counts.most_common(6)]

    # Clean the full summary (strip think tags, leading/trailing whitespace)
    clean_summary = ""
    if theme_sentence:
        clean_summary = re.sub(r"<think>.*?</think>", "", theme_sentence, flags=re.DOTALL).strip()
        clean_summary = re.sub(r"<[^>]+>", "", clean_summary).strip()

    # First non-empty line used as the highlighted theme callout in the content
    clean_theme = next((ln.strip() for ln in clean_summary.splitlines() if ln.strip()), "")
    # Convert inline Markdown to HTML for use inside a raw HTML <span>
    # Escape HTML special chars first, then apply bold/italic so tags aren't double-escaped
    _theme_escaped = _html.escape(clean_theme, quote=False)
    clean_theme_html = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", _theme_escaped)
    clean_theme_html = re.sub(r"\*(.+?)\*", r"<em>\1</em>", clean_theme_html)

    # Build YAML literal block for the full summary (used in page-hero digest-summary)
    if clean_summary:
        summary_block = "summary: |\n" + "\n".join(f"  {ln}" for ln in clean_summary.splitlines())
    else:
        summary_block = 'summary: ""'

    # Build github_trending_topics YAML list
    if gh_top_topics:
        gh_topics_yaml = (
            "github_trending_topics: [" + ", ".join(f'"{t}"' for t in gh_top_topics) + "]"
        )
    else:
        gh_topics_yaml = "github_trending_topics: []"

    lines = [
        "---",
        "layout: modern",
        f'title: "Daily Digest {digest_date}"',
        f"date: {digest_date}",
        f"permalink: /digest/{digest_date}/",
        f"has_papers: {'true' if papers else 'false'}",
        f"has_news: {'true' if regular_news else 'false'}",
        f"has_github_trending: {'true' if gh_items else 'false'}",
        f"paper_count: {len(papers)}",
        f"news_count: {len(regular_news)}",
        f"github_trending_count: {len(gh_items)}",
        'papers_anchor: "global-trends"',
        'github_trending_anchor: "github-trending"',
        summary_block,
        gh_topics_yaml,
        "---",
        "",
    ]

    if clean_theme:
        lines += [
            '<div class="digest-theme">',
            '  <svg class="digest-theme-icon" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true">'
            '<path d="M8 1.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13zM0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8z"/>'
            '<path d="M6.5 7.75A.75.75 0 0 1 7.25 7h1a.75.75 0 0 1 .75.75v2.75h.25a.75.75 0 0 1 0 1.5h-2a.75.75 0 0 1 0-1.5h.25v-2h-.25a.75.75 0 0 1-.75-.75zM8 6a1 1 0 1 1 0-2 1 1 0 0 1 0 2z"/></svg>',
            f"  <span>{clean_theme_html}</span>",
            "</div>",
            "",
        ]

    # ── Section 1: Global Trends ──────────────────────────────────────────────
    if subject_papers or topic_papers:
        lines += [
            '<h2 id="global-trends">Global Trends</h2>',
            "",
        ]

    # ── Subsection 1a: ArXiv subject-category papers ──────────────────────────
    if subject_papers:
        lines += [
            '<h3 id="arxiv-subjects">Papers discovered from ArXiv subject categories</h3>',
            "",
        ]
        for topic in sorted(subject_by_topic):
            papers_in_topic = subject_by_topic[topic]
            if not papers_in_topic:
                continue
            lines += [f"#### {topic}", ""]
            for p in papers_in_topic:
                lines.append(render_paper(p))

    # ── Subsection 1b: Personal Interests (keyword search) ────────────────────
    if topic_papers:
        lines += [
            '<h3 id="personal-interests">Personal Interests</h3>',
            "",
            '<p class="section-desc">Papers discovered through your interest topics.</p>',
            "",
        ]
        for interest in sorted(topic_by_interest):
            papers_in_interest = topic_by_interest[interest]
            if not papers_in_interest:
                continue
            lines += [f"#### {interest}", ""]
            for p in papers_in_interest:
                lines.append(render_paper(p))

    # ── Tech News ─────────────────────────────────────────────────────────────
    if regular_news:
        lines += ['<h2 id="tech-news">Tech News</h2>', ""]
        for topic in sorted(news_by_topic):
            news_in_topic = news_by_topic[topic]
            if not news_in_topic:
                continue
            lines += [f"### {topic}", ""]
            for n in news_in_topic:
                lines.append(render_news_item(n))

    # ── GitHub Trending ───────────────────────────────────────────────────────
    if gh_items:
        lines += [
            '<h2 id="github-trending">',
            '  <svg viewBox="0 0 16 16" fill="currentColor" aria-hidden="true" width="20" height="20" style="vertical-align:middle;margin-right:6px"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>',
            "  GitHub Trending",
            "</h2>",
            "",
            '<p class="section-desc">Trending repositories on GitHub filtered and scored for relevance to your interests.</p>',
            "",
        ]
        for topic in sorted(gh_by_topic):
            repos_in_topic = gh_by_topic[topic]
            if not repos_in_topic:
                continue
            lines += [f"### {topic}", ""]
            for r in repos_in_topic:
                lines.append(render_github_trending_item(r))

    return "\n".join(lines)
