# AI Digest Daily

<div align="center">

<img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white" />
<img src="https://img.shields.io/badge/Jekyll-CC0000?logo=jekyll&logoColor=white" />
<img src="https://img.shields.io/badge/OpenAI-412991?logo=openai&logoColor=white" />
<img src="https://img.shields.io/badge/GitHub_Actions-2088FF?logo=githubactions&logoColor=white" />
<img src="https://img.shields.io/badge/Telegram-26A5E4?logo=telegram&logoColor=white" />
<img src="https://img.shields.io/badge/ArXiv-B31B1B?logo=arxiv&logoColor=white" />

</div>

<br>
> A personal, automated intelligence pipeline that aggregates ArXiv research papers and tech news, processes them with an LLM, and publishes structured daily and weekly digests to a GitHub Pages site — with a Telegram push for on-the-go reading.

---

## Project Overview

Keeping up with AI/ML research and tech news is a full-time job. ArXiv alone publishes hundreds of papers per day across `cs.AI`, `cs.LG`, `cs.CV`, `cs.CL`, and `cs.RO`. Manually filtering signal from noise is exhausting.

**AI Digest Daily** automates the entire curation loop:

1. Every morning it fetches new ArXiv papers and RSS news from curated sources
2. Low-signal papers are pruned early using a Semantic Scholar **h-index prefilter** — before any LLM call is made
3. An LLM scores relevance, categorises each item by topic, and generates structured insight blocks for papers
4. Everything is persisted to a local **SQLite database** for deduplication and weekly rollups
5. The day's results are rendered to **Markdown**, committed to GitHub Pages, and pushed as a **Telegram message**

The system runs entirely on a **self-hosted GitHub Actions runner**, so the SQLite database survives between runs naturally — no cloud database required.

---

## Features

### Research Pipeline (ArXiv)

| Step | What happens |
|---|---|
| **Fetch** | ArXiv RSS API queried for new submissions across all configured categories |
| **Dedup** | Each `arxiv_id` is checked against SQLite before any processing begins |
| **H-index filter** | Semantic Scholar API fetches author h-indexes; papers with no high-h-index author are dropped, saving LLM budget |
| **Author watchlist** | Papers by watched authors receive an automatic relevance boost |
| **LLM pass 1 — Scoring** | Papers are batched and sent to the LLM; each returns `{arxiv_id, relevance 1–5, topic_category}` as JSONL |
| **LLM pass 2 — Insights** | Papers above the relevance cutoff receive a full structured insight block: contribution, core idea, technique, pipeline, methodology, results, limitations |
| **Code detection** | Abstract is scanned for GitHub URLs; Papers With Code API queried for official repositories |
| **Persist** | Results written to the `papers` table; `embedding` column reserved (NULL) for V2 RAG |

### News Pipeline

| Step | What happens |
|---|---|
| **Fetch** | All enabled RSS sources polled for items newer than the previous run window |
| **Dedup** | URL deduplicated against SQLite before LLM calls |
| **LLM summarise** | Single call per item returns `{summary, tags, topic_category, relevance 1–5}` |
| **Filter & persist** | Items below relevance cutoff are discarded; the rest are written to `news_items` |

### Delivery

- **GitHub Pages** — Daily digest and weekly rollup pages committed and deployed on every run
- **Telegram** — Numbered list of paper titles with ArXiv links + news headlines pushed to a private bot; weekly push includes the LLM-generated narrative paragraph
- **Weekly rollup** — Every Sunday, a separate workflow queries the week's DB entries, generates a 4–5 sentence narrative with the LLM, and publishes a rollup page

### Site

- **Reading progress bar** — 3 px accent bar fixed to the top, filled by 8 lines of vanilla JS
- **Page fade-in** — 300 ms ease-in with 6 px upward drift, CSS only
- **Smooth `<details>` expand** — `max-height` transition, no snap-open
- **Tag hover** — background color shift in 150 ms
- **Relevance dots** — `●●●○○` visual scannable score (no numbers needed)
- **GitHub code badge** — Shields.io badge linking directly to the paper's code repository when available

---

## Technology Stack

### Python Backend

| Library | Role |
|---|---|
| `feedparser` | Parse ArXiv RSS and all news RSS/Atom feeds with one unified interface |
| `openai` | OpenAI-compatible client used for both the self-hosted vLLM endpoint and the Azure OpenAI fallback |
| `requests` | Synchronous HTTP for Semantic Scholar API, Papers With Code API, and Telegram Bot API |
| `PyYAML` | Load `config.yaml` — user preferences, source list, topic categories |
| `python-dotenv` | Inject secrets from `.env` at runtime, keeping credentials out of version control |
| `retry` | Transparent retry decorator on flaky external API calls (Semantic Scholar, ArXiv RSS) |
| `tqdm` | Progress bars during batch operations |
| `sqlite3` | Standard library — no ORM, no migration framework; intentionally minimal |

### LLM Infrastructure

| Component | Detail |
|---|---|
| **Primary** | Self-hosted [vLLM](https://github.com/vllm-project/vllm) endpoint — any OpenAI-compatible model |
| **Fallback 1** | Local [Ollama](https://ollama.com) — used if vLLM is unavailable; endpoint and model configurable via `OLLAMA_ENDPOINT` / `OLLAMA_MODEL` env vars |
| **Fallback 2** | Azure OpenAI — last resort if both primary and Ollama fail |
| **Routing** | Sequential `try/except` per tier — no circuit breaker complexity |
| **Deep model** | ArXiv insight generation pass — higher quality, used once per paper |
| **Fast model** | Relevance scoring and news summarisation — throughput-optimised |

### Site

| Component | Detail |
|---|---|
| [Jekyll](https://jekyllrb.com/) | Static site generator; Markdown files from the pipeline become HTML pages at deploy time |
| [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) | Jekyll theme providing layout, typography, and responsive design |
| `peaceiris/actions-gh-pages` | GitHub Action that publishes `site/` to the `gh-pages` branch on every pipeline run |

### External APIs

| API | Used for |
|---|---|
| ArXiv RSS | Source of new paper submissions — official feed, no scraping |
| Semantic Scholar | Author h-index lookup for prefiltering; watched-author matching |
| Papers With Code | Code repository lookup per paper (official repo, sorted by stars) |
| Telegram Bot API | Outbound-only push for daily and weekly summaries |

---

## Architecture

The project is structured as two independent pipelines sharing a common database, LLM client, and rendering layer.

```text
ai-digest-daily/
├── src/
│   ├── configs/
│   │   ├── config.yaml          ← user preferences (sources, categories, cutoffs)
│   │   └── authors.txt          ← watched Semantic Scholar author IDs
│   │
│   ├── db/
│   │   └── database.py          ← SQLite init, upsert, dedup helpers
│   │
│   ├── llm/
│   │   ├── client.py            ← primary vLLM → Ollama → Azure fallback routing
│   │   ├── prompts.py           ← all prompt templates (scoring, insights, news, narrative)
│   │   └── scoring.py           ← batched relevance scoring + JSONL parser
│   │
│   ├── pipelines/
│   │   ├── arxiv_pipeline.py    ← fetch → filter → score → code lookup → insights → DB
│   │   └── news_pipeline.py     ← fetch → dedup → summarise → DB
│   │
│   ├── render/
│   │   ├── daily.py             ← daily digest Markdown with relevance dots + code badges
│   │   └── weekly.py            ← weekly rollup Markdown with narrative blockquote
│   │
│   ├── delivery/
│   │   └── telegram.py          ← outbound Telegram push (daily + weekly)
│   │
│   ├── main.py                  ← daily entrypoint  →  python -m src.main
│   └── weekly_main.py           ← weekly entrypoint →  python -m src.weekly_main
│
├── site/                        ← Jekyll source (pushed to gh-pages on each run)
│   ├── _config.yml
│   ├── _posts/                  ← generated daily digest pages land here
│   ├── _weekly/                 ← generated weekly rollup pages land here
│   ├── _pages/                  ← static pages: archive, papers, news, weekly index
│   ├── assets/css/digest.css    ← progress bar, fade-in, transitions
│   └── assets/js/progress.js   ← 8-line scroll progress bar
│
├── .github/workflows/
│   ├── daily.yml                ← cron 03:00 UTC (10:00 UTC+7), self-hosted runner
│   └── weekly.yml               ← cron Sunday 20:00 UTC, self-hosted runner
│
├── digest/                      ← gitignored; SQLite DB lives here
└── .env                         ← secrets, never committed
```

### Data Flow

```text
          ArXiv RSS ──────┐
                          ▼
                    fetch_arxiv_rss()
                          │
                    dedup vs SQLite ──── (already seen → skip)
                          │
                  Semantic Scholar API
                  (h-index filter)
                          │
                    LLM pass 1
                  (batch scoring)
                          │
                relevance cutoff ──── (score < 2 → drop)
                          │
                  Papers With Code
                  (code URL lookup)
                          │
                    LLM pass 2
                (per-paper insights)
                          │
                    upsert_paper()
                          │
          RSS Feeds ──────┐
                          ▼
                   fetch_rss_feed()
                          │
                    dedup vs SQLite
                          │
                    LLM summarise
                          │
                relevance cutoff
                          │
                  upsert_news_item()
                          │
                    render_daily()
                          │
               site/_posts/YYYY-MM-DD.md
                          │
               GitHub Pages deploy ──► telegram.push_daily()
```

### Database Schema

**`papers`**

| Column | Type | Notes |
|---|---|---|
| `arxiv_id` | TEXT PK | Deduplication key |
| `title` | TEXT | |
| `authors` | TEXT | Comma-separated |
| `abstract` | TEXT | Raw from ArXiv |
| `categories` | TEXT | ArXiv categories |
| `topic_category` | TEXT | LLM-assigned |
| `relevance` | INTEGER | 1–5 |
| `insights` | TEXT | JSON blob (7 structured fields) |
| `code_url` | TEXT | GitHub repo URL if found |
| `published_date` | TEXT | |
| `fetched_date` | TEXT | |
| `digest_date` | TEXT | |
| `digest_week` | INTEGER | ISO week — enables weekly rollup queries |
| `embedding` | BLOB | NULL in V1, reserved for V2 RAG backfill |

**`news_items`**

| Column | Type | Notes |
|---|---|---|
| `url` | TEXT PK | Deduplication key |
| `title` | TEXT | |
| `source` | TEXT | Source name from config |
| `summary` | TEXT | LLM-generated, 2–4 sentences |
| `tags` | TEXT | Comma-separated |
| `topic_category` | TEXT | LLM-assigned |
| `relevance` | INTEGER | 1–5 |
| `published_date` | TEXT | |
| `fetched_date` | TEXT | |
| `digest_date` | TEXT | |
| `digest_week` | INTEGER | ISO week |
| `embedding` | BLOB | NULL in V1 |

### LLM Routing

```text
complete(prompt)
    │
    ├─ try: POST vLLM endpoint (self-hosted)
    │        └─ success → return response
    │
    ├─ except: POST Ollama (localhost:11434, fallback 1)
    │           └─ success → return response
    │
    └─ except: POST Azure OpenAI (fallback 2)
               └─ return response
```

No retry loops, no circuit breaker — sequential `try/except` per tier. Simple and auditable.
Ollama endpoint and model are configurable via `OLLAMA_ENDPOINT` and `OLLAMA_MODEL` env vars (defaults: `http://localhost:11434/v1`, `qwen2.5:7b`).

---

## Getting Started

### Prerequisites

- Python 3.10+
- Ruby + Bundler (for local site preview only)
- A self-hosted GitHub Actions runner (for scheduled runs with persistent SQLite)

### 1. Clone and install

```bash
git clone https://github.com/hiimmuc/ai-digest-daily
cd ai-digest-daily
pip install -r requirements.txt
```

### 2. Configure secrets

```bash
cp .env.example .env
# Edit .env — minimum required: AZURE_OPENAI_* keys
# VLLM_ENDPOINT is optional; falls back to Ollama then Azure automatically
# OLLAMA_ENDPOINT / OLLAMA_MODEL are optional (defaults: localhost:11434, qwen2.5:7b)
```

### 3. Configure preferences

Edit `src/configs/config.yaml` to set:

- ArXiv categories and relevance cutoffs
- News RSS sources (enable/disable per source)
- Telegram delivery toggle
- Topic categories for LLM classification

Optionally add watched author IDs to `src/configs/authors.txt`:

```text
# Name, Semantic Scholar Author ID
Yann LeCun, 1741101
```

### 4. Run

```bash
# Daily pipeline (ArXiv + News → DB → Markdown → Telegram)
python -m src.main

# Weekly rollup (query DB → narrative → Markdown → Telegram)
python -m src.weekly_main

# Preview the Jekyll site locally
cd site && bundle install && bundle exec jekyll serve
```

### 5. GitHub Actions (automated)

#### Automated Run Flow

```text
Cron trigger (GitHub Actions)
        ↓
Self-hosted runner wakes up
        ↓
main.py runs both pipelines
        ↓
SQLite updated
        ↓
Markdown digest generated
        ↓
Committed to gh-pages branch
        ↓
GitHub Pages deploys automatically
        ↓
Telegram push sent
```

#### Self-Hosted Runner Setup

The pipeline requires a **self-hosted runner** so that the SQLite database persists between runs (GitHub-hosted runners are ephemeral and would lose the DB on every run).

1. **Register a runner** on your machine:

   ```bash
   # Download from: Settings → Actions → Runners → New self-hosted runner
   mkdir actions-runner && cd actions-runner
   curl -o actions-runner-linux-x64.tar.gz -L https://github.com/actions/runner/releases/latest/download/actions-runner-linux-x64.tar.gz
   tar xzf actions-runner-linux-x64.tar.gz
   ./config.sh --url https://github.com/<owner>/<repo> --token <RUNNER_TOKEN>
   ```

2. **Install as a systemd service** so it survives reboots:

   ```bash
   sudo ./svc.sh install
   sudo ./svc.sh start
   # Check status
   sudo ./svc.sh status
   ```

3. **Verify** the runner appears as **Idle** under *Settings → Actions → Runners* in your repository.

> The workflows use `runs-on: self-hosted` — GitHub will route all scheduled jobs to this runner automatically.

#### Repository Secrets

Set the following secrets under *Settings → Secrets and variables → Actions*:

| Secret | Required | Description |
|---|---|---|
| `VLLM_ENDPOINT` | Optional | Self-hosted vLLM base URL |
| `VLLM_MODEL` | Optional | Model name on the vLLM instance |
| `OLLAMA_ENDPOINT` | Optional | Ollama base URL (default: `http://localhost:11434/v1`) |
| `OLLAMA_MODEL` | Optional | Ollama model name (default: `qwen2.5:7b`) |
| `AZURE_OPENAI_ENDPOINT` | Required | Azure OpenAI resource URL |
| `AZURE_OPENAI_KEY` | Required | Azure API key |
| `AZURE_OPENAI_MODEL` | Required | Deployment name (e.g. `gpt-4o`) |
| `SEMANTIC_SCHOLAR_KEY` | Optional | S2 API key (avoids rate limits) |
| `TELEGRAM_BOT_TOKEN` | Optional | Bot token from @BotFather |
| `TELEGRAM_CHAT_ID` | Optional | Target chat or channel ID |
