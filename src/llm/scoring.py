"""Relevance scoring via LLM batch calls."""

import json
import logging
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, List

from tqdm import tqdm

from . import client
from .prompts import SCORING_PROMPT

logger = logging.getLogger(__name__)

BATCH_SIZE = 10
MAX_WORKERS = 4  # concurrent API calls


def parse_json_response(text: str) -> dict:
    """Parse a single JSON object from an LLM response, stripping markdown fences."""
    text = re.sub(r"```json\n?", "", text)
    text = re.sub(r"```", "", text).strip()
    return json.loads(text)


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

    def _score_one_batch(batch: List[Dict]) -> List[Dict]:
        papers_text = "\n\n".join(
            f"ArXiv ID: {p['arxiv_id']}\n"
            f"Title: {p['title']}\n"
            f"Abstract: {p['abstract'][:500]}"
            for p in batch
        )
        prompt = SCORING_PROMPT.format(
            topic_categories=", ".join(topic_categories),
            interests=interests,
            papers=papers_text,
        )
        return parse_jsonl(client.complete(prompt))

    batches = [papers[i : i + BATCH_SIZE] for i in range(0, len(papers), BATCH_SIZE)]
    scores: Dict[str, Dict] = {}

    client.try_init()  # fire "Initialising ..." log before the progress bar
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {pool.submit(_score_one_batch, batch): idx for idx, batch in enumerate(batches)}
        for future in tqdm(as_completed(futures), total=len(batches), desc="Scoring batches"):
            try:
                for item in future.result():
                    if "arxiv_id" in item:
                        scores[item["arxiv_id"]] = item
            except Exception as e:
                logger.warning("Scoring batch %d failed: %s", futures[future] + 1, e)
    return scores
