"""Relevance scoring via LLM batch calls."""

import json
import re
from typing import Dict, List

from . import client
from .prompts import SCORING_PROMPT

BATCH_SIZE = 10


def parse_jsonl(text: str) -> List[Dict]:
    """Parse JSONL-style LLM output, tolerating common formatting issues."""
    text = re.sub(r"```json[l]?\n?", "", text)
    text = re.sub(r"```", "", text)
    text = re.sub(r"},\s*\n", "}\n", text)
    results = []
    for line in text.strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        try:
            results.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return results


def score_papers_batch(
    papers: List[Dict], topic_categories: List[str], interests: str
) -> Dict[str, Dict]:
    """Score papers for relevance in batches. Returns dict keyed by arxiv_id."""
    scores: Dict[str, Dict] = {}
    for i in range(0, len(papers), BATCH_SIZE):
        batch = papers[i : i + BATCH_SIZE]
        papers_text = "\n\n".join(
            f"ArXiv ID: {p['arxiv_id']}\n"
            f"Title: {p['title']}\n"
            f"Abstract: {p['abstract'][:1000]}"
            for p in batch
        )
        prompt = SCORING_PROMPT.format(
            topic_categories=", ".join(topic_categories),
            interests=interests,
            papers=papers_text,
        )
        try:
            response = client.complete(prompt)
            for item in parse_jsonl(response):
                if "arxiv_id" in item:
                    scores[item["arxiv_id"]] = item
        except Exception as e:
            print(f"Scoring batch {i // BATCH_SIZE + 1} failed: {e}")
    return scores
