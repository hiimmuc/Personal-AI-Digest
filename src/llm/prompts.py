"""All LLM prompt templates."""

GITHUB_TRENDING_PROMPT = """You are a technical curator selecting GitHub repositories for an AI/ML research digest.

Repository:
  Name:        {name}
  Description: {description}
  Language:    {language}
  Topics:      {topics}
  Stars:       {stars}
  README:      {readme}

User interests: {interests}

Score relevance 1–5:
  1 = unrelated to AI/ML/tech interests
  2 = tangentially related
  3 = moderately relevant
  4 = highly relevant (implements or studies a key interest area)
  5 = must-see (directly advances a core interest)

Topic categories: {topic_categories}

Return ONLY this JSON (no markdown, no extra text):
{{
  "relevance": <1-5>,
  "topic_category": "one category from the list above",
  "summary": "2-3 sentences: what this repo does and why it is relevant",
  "tags": "comma-separated tags (3-5 tags)"
}}"""


SCORING_PROMPT = """You are a research assistant curating AI/ML papers for a personal digest.

Score each paper's relevance on a scale of 1–5:
  1 = completely unrelated
  2 = tangentially related
  3 = moderately relevant
  4 = highly relevant
  5 = must-read

Also assign one topic_category from: {topic_categories}

User interests:
{interests}

Papers:
{papers}

Respond with exactly one JSON object per line (JSONL). Format:
{{"arxiv_id": "...", "relevance": <1-5>, "topic_category": "..."}}

Output ONLY the JSONL, no extra text."""


INSIGHTS_PROMPT = """Generate a structured insight block for this research paper.

Title: {title}
Authors: {authors}
Abstract: {abstract}

Return ONLY this JSON (no markdown, no extra text):
{{
  "contribution": "1-2 sentences on the main contribution",
  "core_idea": "1-2 sentences on the core idea",
  "technique": "1-2 sentences on the main technique",
  "pipeline": "input → process → output in plain text",
  "methodology": "1-2 sentences on the methodology",
  "results": "key quantitative or qualitative results",
  "limitations": "main limitations or open questions"
}}"""


NEWS_PROMPT = """You are a tech news curator for an AI/ML digest.

Analyze this news item:
Source: {source}
Title: {title}
Content: {content}

Topic categories: {topic_categories}

Rate relevance 1–5 (1=not relevant to AI/tech, 5=critical news).

Return ONLY this JSON:
{{
  "url": "{url}",
  "summary": "2-4 sentence summary",
  "tags": "comma-separated tags (3-5 tags)",
  "topic_category": "one category from the list",
  "relevance": <1-5>
}}"""


WEEKLY_NARRATIVE_PROMPT = """Write a 4–5 sentence narrative paragraph summarizing this week in AI and tech.
Be analytical and highlight the most significant themes, developments, and community activity.

Top papers this week:
{papers}

Top news this week:
{news}

Top repos this week:
{repos}

Write only the paragraph, no title or preamble."""


DIGEST_SUMMARY_PROMPT = """You are a technical editor writing a concise overview of today's AI/ML digest. Use plain, analytical language.

Today's papers and news:
{items}

Write a structured Markdown summary in this format:

Begin with 1–2 sentences capturing the dominant theme across today's content (what unifying trend or focus stands out?).

**Research highlights:**
- **[Topic name]**: one sentence on what papers in this area are doing
- (3–5 bullets for topics present in today's papers)

**Tech buzz:**
- one sentence on a notable news item or trend
- (2–3 bullets — omit this entire section if no news items are present)

Rules:
- Write actual content — do not echo these instructions
- Do not mention specific paper titles or URLs
- Bold every topic name in bullets (e.g. **LLMs**, **Robotics**)
- Output only the Markdown, no preamble or explanation"""
