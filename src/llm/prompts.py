"""All LLM prompt templates."""

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
Be analytical and highlight the most significant themes and developments.

Top papers this week:
{papers}

Top news this week:
{news}

Write only the paragraph, no title or preamble."""


THEME_SENTENCE_PROMPT = """In one short sentence (max 15 words), capture the main theme of today's AI/tech digest.

Today's items:
{items}

Write only the sentence."""
