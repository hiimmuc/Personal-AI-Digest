"""SQLite read/write and deduplication helpers."""

import json
import sqlite3
from datetime import date
from pathlib import Path

DB_PATH = Path(__file__).parent.parent.parent / "digest" / "knowledge.db"


def get_connection() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS papers (
                arxiv_id      TEXT PRIMARY KEY,
                title         TEXT,
                authors       TEXT,
                abstract      TEXT,
                categories    TEXT,
                topic_category TEXT,
                relevance     INTEGER,
                insights      TEXT,
                published_date TEXT,
                fetched_date  TEXT,
                digest_date   TEXT,
                digest_week   INTEGER,
                code_url      TEXT DEFAULT '',
                discovery_type TEXT DEFAULT 'subject',
                search_topic  TEXT DEFAULT '',
                embedding     BLOB
            )
        """)
        # Migrations: add columns to existing papers table
        for col, definition in [
            ("code_url", "TEXT DEFAULT ''"),
            ("discovery_type", "TEXT DEFAULT 'subject'"),
            ("search_topic", "TEXT DEFAULT ''"),
        ]:
            try:
                conn.execute(f"ALTER TABLE papers ADD COLUMN {col} {definition}")
            except Exception:
                pass  # column already exists
        conn.execute("""
            CREATE TABLE IF NOT EXISTS news_items (
                url           TEXT PRIMARY KEY,
                title         TEXT,
                source        TEXT,
                summary       TEXT,
                tags          TEXT,
                topic_category TEXT,
                relevance     INTEGER,
                published_date TEXT,
                fetched_date  TEXT,
                digest_date   TEXT,
                digest_week   INTEGER,
                stars         INTEGER DEFAULT 0,
                embedding     BLOB
            )
        """)
        # Migrations: add columns to existing news_items table
        try:
            conn.execute("ALTER TABLE news_items ADD COLUMN stars INTEGER DEFAULT 0")
        except Exception:
            pass  # column already exists
        conn.commit()


def paper_exists(arxiv_id: str) -> bool:
    with get_connection() as conn:
        return (
            conn.execute("SELECT 1 FROM papers WHERE arxiv_id = ?", (arxiv_id,)).fetchone()
            is not None
        )


def news_exists(url: str) -> bool:
    with get_connection() as conn:
        return (
            conn.execute("SELECT 1 FROM news_items WHERE url = ?", (url,)).fetchone() is not None
        )


def upsert_paper(paper: dict):
    today = date.today().isoformat()
    week = date.today().isocalendar()[1]
    with get_connection() as conn:
        conn.execute(
            """
            INSERT OR REPLACE INTO papers
            (arxiv_id, title, authors, abstract, categories, topic_category,
             relevance, insights, published_date, fetched_date, digest_date, digest_week,
             code_url, discovery_type, search_topic, embedding)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NULL)
            """,
            (
                paper["arxiv_id"],
                paper.get("title", ""),
                paper.get("authors", ""),
                paper.get("abstract", ""),
                paper.get("categories", ""),
                paper.get("topic_category", ""),
                paper.get("relevance", 0),
                json.dumps(paper.get("insights", {})),
                paper.get("published_date", ""),
                today,
                today,
                week,
                paper.get("code_url", ""),
                paper.get("discovery_type", "subject"),
                paper.get("search_topic", ""),
            ),
        )
        conn.commit()


def upsert_news_item(item: dict):
    today = date.today().isoformat()
    week = date.today().isocalendar()[1]
    with get_connection() as conn:
        conn.execute(
            """
            INSERT OR REPLACE INTO news_items
            (url, title, source, summary, tags, topic_category, relevance,
             published_date, fetched_date, digest_date, digest_week, stars, embedding)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, NULL)
            """,
            (
                item["url"],
                item.get("title", ""),
                item.get("source", ""),
                item.get("summary", ""),
                item.get("tags", ""),
                item.get("topic_category", ""),
                item.get("relevance", 0),
                item.get("published_date", ""),
                today,
                today,
                week,
                item.get("stars", 0),
            ),
        )
        conn.commit()


def get_papers_for_date(digest_date: str) -> list:
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM papers WHERE digest_date = ? ORDER BY relevance DESC",
            (digest_date,),
        ).fetchall()
        return [dict(row) for row in rows]


def get_news_for_date(digest_date: str) -> list:
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM news_items WHERE digest_date = ? ORDER BY relevance DESC",
            (digest_date,),
        ).fetchall()
        return [dict(row) for row in rows]


def get_papers_for_week(digest_week: int) -> list:
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM papers WHERE digest_week = ? ORDER BY relevance DESC",
            (digest_week,),
        ).fetchall()
        return [dict(row) for row in rows]


def get_news_for_week(digest_week: int) -> list:
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM news_items WHERE digest_week = ? AND source != 'GitHub Trending' ORDER BY relevance DESC",
            (digest_week,),
        ).fetchall()
        return [dict(row) for row in rows]


def get_repos_for_week(digest_week: int) -> list:
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM news_items WHERE digest_week = ? AND source = 'GitHub Trending' ORDER BY stars DESC, relevance DESC",
            (digest_week,),
        ).fetchall()
        return [dict(row) for row in rows]
