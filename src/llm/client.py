"""LLM client: vLLM -> Ollama -> Azure OpenAI with lazy init and backend caching."""

import logging
import os
import re
from typing import Callable, Optional, Tuple

logger = logging.getLogger(__name__)

from openai import AzureOpenAI, OpenAI

_THINK_RE = re.compile(r"<think>.*?</think>", re.DOTALL)


def _strip_thinking(text: str) -> str:
    return _THINK_RE.sub("", text).strip()


class _Backend:
    """Lazily-initialised LLM backend. Client is created on first use."""

    def __init__(
        self, name: str, factory: Callable[[], Tuple], max_tokens: Optional[int] = None
    ) -> None:
        self.name = name
        self._factory = factory
        self._max_tokens = max_tokens
        self._instance: Optional[Tuple] = None

    def _get(self) -> Tuple:
        if self._instance is None:
            self._instance = self._factory()
        return self._instance

    def complete(self, prompt: str) -> str:
        client, model = self._get()
        kwargs: dict = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.0,
        }
        if self._max_tokens is not None:
            kwargs["max_tokens"] = self._max_tokens
        resp = client.chat.completions.create(**kwargs)
        content = _strip_thinking(resp.choices[0].message.content or "")
        if not content:
            raise ValueError(f"{self.name} returned empty content")
        return content


def _build_backends() -> list:
    def vllm():
        endpoint = os.environ.get("VLLM_ENDPOINT", "")
        if not endpoint:
            raise ValueError("VLLM_ENDPOINT not set")
        model = os.environ.get("VLLM_MODEL", "")
        logger.info("Initialising vLLM: endpoint=%s model=%s", endpoint, model)
        return OpenAI(base_url=endpoint, api_key="dummy"), model

    def ollama():
        endpoint = os.environ.get("OLLAMA_ENDPOINT", "http://localhost:11434/v1")
        model = os.environ.get("OLLAMA_MODEL", "qwen3:14b")
        logger.info("Initialising Ollama: endpoint=%s model=%s", endpoint, model)
        return OpenAI(base_url=endpoint, api_key="ollama"), model

    def azure():
        return (
            AzureOpenAI(
                azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
                api_key=os.environ["AZURE_OPENAI_KEY"],
                api_version="2024-02-01",
            ),
            os.environ["AZURE_OPENAI_MODEL"],
        )

    return [
        _Backend("vLLM", vllm, max_tokens=4096),
        _Backend("Ollama", ollama, max_tokens=8192),
        _Backend("Azure", azure),
    ]


_backends = _build_backends()
_active_idx: int = -1  # index of the last known-working backend


def try_init() -> None:
    """Eagerly create client objects for all backends (no API calls).

    Call this before a tqdm loop so the "Initialising ..." log fires before
    the progress bar starts, not inside it.
    """
    for backend in _backends:
        try:
            backend._get()
        except Exception:
            pass


def complete(prompt: str) -> str:
    """Call the first available backend; remember it to skip re-discovery."""
    global _active_idx

    if _active_idx >= 0:
        return _backends[_active_idx].complete(prompt)

    last = len(_backends) - 1
    for i, backend in enumerate(_backends):
        try:
            result = backend.complete(prompt)
            _active_idx = i
            return result
        except Exception as e:
            if i < last:
                logger.warning("%s failed (%s), trying next backend...", backend.name, e)
            else:
                raise
