# Personal AI Assistant — Tech News & Research Aggregation

## Project Implementation Instruction (V1)

---

## Overview

A personal, automated daily/weekly tech intelligence tool. It collects ArXiv papers and general tech news, processes them with an LLM, stores results in a local SQLite database, and publishes structured digests to a GitHub Pages site with a secondary Telegram push.

- **User:** Single user, personal use only
- **Language:** English only
- **V1 scope:** No RAG, no chatbot, no knowledge graph
- **Deployment:** Self-hosted GitHub Actions runner on local machine

---

## Two Parallel Pipelines

### Pipeline 1 — ArXiv Research

**Source:** ArXiv RSS API (official, no scraping).

**Steps:**

1. Fetch new papers for configured categories (e.g., `cs.AI`, `cs.LG`, `cs.RO`, `cs.CV`, `cs.CL`)
2. Check each paper's ArXiv ID against SQLite — skip if already processed
3. Filter by h-index cutoff via Semantic Scholar API (drops low-signal papers before LLM calls)
4. Author match check via Semantic Scholar — papers matching watched authors get a score boost
5. LLM pass 1 — relevance scoring: batch papers, return `{arxiv_id, relevance: 1-5, topic_category}` per paper in JSON
6. Drop papers below configured relevance cutoff (e.g., `< 2`)
7. LLM pass 2 — insights: per remaining paper, generate structured insight block:
   - Contribution / Core idea / Main technique
   - Architecture / Pipeline / Workflow (plain text, input → process → output)
   - Methodology summary
   - Significant results / findings
   - Limitations
8. Write to SQLite `papers` table
9. Render to Markdown for GitHub Pages

**Reference:** <https://github.com/JackYFL/gpt_paper_assistant>

---

### Pipeline 2 — General News

**Source:** RSS feeds and light scraping for 5–10 curated sources (Reddit r/MachineLearning, Hacker News, NVIDIA Technical Blog, GitHub Trending, Google News AI filter, etc.). Per-source config in `.yaml`.

**Steps:**

1. Fetch new items per source
2. Deduplicate by URL against SQLite
3. LLM pass — single call per item: return `{url, summary (2–4 sentences), tags, topic_category, relevance: 1-5}`
4. Drop items below relevance cutoff
5. Write to SQLite `news_items` table
6. Render to Markdown for GitHub Pages

**Reference:** <https://github.com/Thysrael/Horizon>

---

## LLM Configuration

Configured via `.env` (secrets stay out of version control):

- **Primary:** Self-hosted vLLM endpoint
- **Fallback:** Azure OpenAI

Two model configs:

- **Deep analysis model** — ArXiv insights pass
- **Fast summarization model** — news items, relevance scoring pass

The pipeline tries primary, catches timeout/error, falls back to Azure. A single try/except wrapping the HTTP call handles routing — no complex logic.

---

## Database

**SQLite**, stored on local machine. Self-hosted GitHub Actions runner means the DB file persists between runs naturally.

### `papers` table

| Column | Type | Notes |
|---|---|---|
| arxiv_id | TEXT PRIMARY KEY | Deduplication key |
| title | TEXT | |
| authors | TEXT | Comma-separated |
| abstract | TEXT | Raw from ArXiv |
| categories | TEXT | ArXiv categories |
| topic_category | TEXT | LLM-assigned from config list |
| relevance | INTEGER | 1–5 |
| insights | JSON | Structured insight block fields |
| published_date | DATE | |
| fetched_date | DATE | |
| digest_date | DATE | |
| digest_week | INTEGER | ISO week number, for weekly rollup |
| embedding | BLOB | NULL in V1, reserved for V2 RAG |

### `news_items` table

| Column | Type | Notes |
|---|---|---|
| url | TEXT PRIMARY KEY | Deduplication key |
| title | TEXT | |
| source | TEXT | Source name from config |
| summary | TEXT | 2–4 sentences, LLM-generated |
| tags | TEXT | Comma-separated |
| topic_category | TEXT | LLM-assigned from config list |
| relevance | INTEGER | 1–5 |
| published_date | DATE | |
| fetched_date | DATE | |
| digest_date | DATE | |
| digest_week | INTEGER | ISO week number |
| embedding | BLOB | NULL in V1, reserved for V2 RAG |

### Key behaviors

- Deduplication on `arxiv_id` and `url` before any LLM call is made
- `digest_week` enables weekly rollup queries without extra data structures
- `insights` stored as JSON so individual fields are queryable later without schema migration
- `embedding` column present but NULL — V2 RAG migration is a backfill, not a schema change
- Human-readable export: each run renders the day's DB entries to Markdown (GitHub Pages source) — DB and human-readable format stay in sync automatically

---

## GitHub Pages Site

### Stack

Jekyll + Minimal Mistakes — same as portfolio at <https://hiimmuc.github.io/>. Inherits typography, spacing, and accent color with no additional configuration.

### Routes

```
/                   → Today's digest (default landing)
/archive/           → Reverse chronological digest index
/weekly/            → Weekly rollup pages
/papers/            → All-time papers index
/news/              → All-time news index
```

### Favicon

Minimal custom SVG monogram (single letter or two-letter mark), accent color, 32×32, no icon library. Served as `favicon.svg`.

### Reading Progress Bar

A 2–3px bar fixed to the very top of the viewport, above navigation. Fills left-to-right as the user scrolls. Accent color. Implemented as a single `<div id="progress">` updated by ~8 lines of inline JS reading `window.scrollY`.

### Animated Transitions

Three transitions, all CSS-only or near-CSS:

1. **Page load fade-in:** Main content wrapper fades in over 300ms with a 6px upward drift

   ```css
   .page__content { animation: fadeIn 0.3s ease-in; }
   @keyframes fadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; } }
   ```

2. **`<details>` expand:** Smooth `max-height` transition on the inner container — no snap-open
3. **Tag hover:** Background color shift, `transition: background 0.15s ease` — no movement

If all animations were removed, the site would still feel complete. That is the constraint.

---

### Daily Digest Page Layout

```text
[Date]  ·  [Theme sentence — LLM generated, 1 line, muted style]
──────────────────────────────────────────────────────────────────
[Sort by: Most Recent | Most Relevance]          ← plain text toggles

## Research Papers

### LLM
  [R: ●●●●○]  cs.AI · cs.LG                           2025-05-23
  Title of the Paper
  Authors: A, B, C  ·  arxiv.org/abs/xxxx

  <details> Abstract </details>
  <details> Insights </details>

  ─────────────

  [next paper...]

### Computer Vision
  [papers...]

### Robotics
  [papers...]

## Tech News

### LLM
  [Hacker News]  2025-05-23
  Headline title as a link

  2–3 sentence LLM summary.
  tag1 · tag2 · tag3

  ─────────────

  [next item...]

### MLOps
  [items...]
```

**Design notes:**

- Relevance shown as filled/empty dots (●●●●○) — scannable without reading numbers
- Topic categories are `<h3>` headers within each section
- Sort toggles are plain text links — no styled button components
- `<details>` blocks have a left-border accent (`border-left: 2px solid <accent>`) when open
- `<hr>` separators match the weight of portfolio section dividers

---

### Archive Index

Mirrors the portfolio blog year-archive. Grouped by month, one line per digest:

```
May 2026
  23 May — Daily Digest     (8 papers · 6 news)
  Week 21 — Weekly Rollup
  22 May — Daily Digest     (11 papers · 9 news)
```

---

### Weekly Rollup Page

Same layout as a daily digest page. Opens with a 4–5 sentence LLM-generated narrative paragraph in a blockquote style before the items. Items are the top-scored entries from the week, linked back to their original daily digest page. Week number and date range replace the single date in the page header.

---

## Delivery

### GitHub Pages — Primary

Rendered and committed automatically on each pipeline run. The `gh-pages` branch is the deploy source. GitHub Pages auto-deploys on every push.

### Telegram — Secondary (outbound only in V1)

- **Daily push:** Numbered list of paper titles with ArXiv links, then news headlines with source labels
- **Weekly push:** Top N items by relevance from the week + the LLM weekly narrative sentence

No interaction, no webhook handling in V1. The bot token/infrastructure is in place for V2 Q&A addition.

---

## Scheduling — GitHub Actions

Two workflows, running on a **self-hosted runner** (local machine) to preserve SQLite persistence.

### Daily workflow (`daily.yml`) — e.g., 06:00 UTC

1. Run both pipelines (ArXiv + News)
2. Write results to SQLite
3. Generate day's Markdown digest
4. Commit to `gh-pages` branch → GitHub Pages auto-deploys
5. Push Telegram daily message

### Weekly workflow (`weekly.yml`) — Sunday 20:00 UTC

1. Query SQLite for `digest_week = current_week`
2. Rank all items by relevance
3. LLM generates weekly narrative paragraph
4. Generate weekly rollup Markdown, commit to `gh-pages`
5. Push Telegram weekly message

---

## Configuration Files

### `.yaml` — User preferences (committed to repo)

```yaml
arxiv:
  categories: [cs.AI, cs.LG, cs.RO, cs.CV, cs.CL]
  max_papers_per_day: 30
  relevance_cutoff: 2          # drop papers below this score
  hindex_cutoff: 10            # Semantic Scholar h-index prefilter
  author_watchlist: configs/authors.txt

topic_categories:
  - LLM
  - Computer Vision
  - Robotics
  - Speech
  - RL
  - MLOps

news:
  relevance_cutoff: 2
  sources:
    - name: Hacker News
      type: rss
      url: https://news.ycombinator.com/rss
      enabled: true
    - name: NVIDIA Technical Blog
      type: rss
      url: https://developer.nvidia.com/blog/feed
      enabled: true
    - name: Reddit r/MachineLearning
      type: rss
      url: https://www.reddit.com/r/MachineLearning/.rss
      enabled: true
    # Add up to 10 sources total

delivery:
  telegram_enabled: true
  github_pages_repo: username/digest-site
  daily_time_utc: "06:00"
  weekly_day: Sunday

site:
  title: "AI Digest"
  sort_default: recent         # recent | relevance
```

### `.env` — Secrets (never committed, add to `.gitignore`)

```env
VLLM_ENDPOINT=http://localhost:8000/v1
VLLM_MODEL=your-model-name
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_KEY=your-azure-key
AZURE_OPENAI_MODEL=gpt-4o
SEMANTIC_SCHOLAR_KEY=your-s2-key
TELEGRAM_BOT_TOKEN=your-bot-token
TELEGRAM_CHAT_ID=your-chat-id
```

---

## Repository Structure

```text
src/
├── configs/
│   ├── config.yaml              # user preferences
│   └── authors.txt              # watched author IDs (Semantic Scholar)
├── pipelines/
│   ├── arxiv_pipeline.py        # ArXiv fetch, filter, score, insights
│   └── news_pipeline.py         # RSS/scrape fetch, summarize, score
├── llm/
│   ├── client.py                # primary/fallback endpoint routing
│   ├── prompts.py               # all prompt templates
│   └── scoring.py               # relevance scoring logic
├── db/
│   └── database.py              # SQLite read/write, dedup helpers
├── render/
│   ├── daily.py                 # generates daily digest Markdown
│   └── weekly.py                # generates weekly rollup Markdown
├── delivery/
│   └── telegram.py              # outbound Telegram push
├── main.py                      # daily pipeline entrypoint
├── weekly_main.py               # weekly rollup entrypoint
├── requirements.txt
├── .env                         # secrets — never committed
├── .gitignore                   # includes .env and digest/
├── .github/
│   └── workflows/
│       ├── daily.yml            # daily schedule + deploy
│       └── weekly.yml           # weekly rollup + deploy
└── digest/
    └── knowledge.db             # SQLite DB — local only, gitignored
```

---

## V2 Hooks (Intentional Decisions to Avoid Rework)

The following decisions are made in V1 specifically to make V2 non-breaking:

| Decision | Why |
|---|---|
| `insights` stored as JSON (not flat text) | Individual fields queryable for RAG without schema changes |
| `embedding BLOB` column present but NULL | RAG migration is a backfill job, not a schema migration |
| `topic_category` field from day one | Enables future filtering, trend queries, and graph structure |
| Telegram bot outbound-only but token wired up | Adding Q&A in V2 is purely additive — just add a webhook handler |
| Relevance score (1–5) persisted in DB | Weekly trend tracking and future analytics without reprocessing |

---

## References

- ArXiv pipeline: <https://github.com/JackYFL/gpt_paper_assistant> (forked from <https://github.com/tatsu-lab/gpt_paper_assistant>)
- News pipeline: <https://github.com/Thysrael/Horizon>
- Site styling reference: <https://hiimmuc.github.io/>
