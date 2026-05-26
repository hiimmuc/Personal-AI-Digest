"""LLM client: primary vLLM endpoint with Ollama and Azure OpenAI fallbacks."""

import os
import re

from openai import AzureOpenAI, OpenAI

_THINK_RE = re.compile(r"<think>.*?</think>", re.DOTALL)


def _strip_thinking(text: str) -> str:
    """Remove <think>...</think> reasoning blocks emitted by thinking models."""
    return _THINK_RE.sub("", text).strip()


def _primary_client():
    endpoint = os.environ.get("VLLM_ENDPOINT", "")
    if not endpoint:
        raise ValueError("VLLM_ENDPOINT is not set")
    model = os.environ.get("VLLM_MODEL", "")
    client = OpenAI(base_url=endpoint, api_key="dummy")
    return client, model


def _ollama_client():
    endpoint = os.environ.get("OLLAMA_ENDPOINT", "http://localhost:11434/v1")
    model = os.environ.get("OLLAMA_MODEL", "qwen3.5:latest")
    client = OpenAI(base_url=endpoint, api_key="ollama")
    return client, model


def _azure_client():
    endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
    key = os.environ["AZURE_OPENAI_KEY"]
    model = os.environ["AZURE_OPENAI_MODEL"]
    client = AzureOpenAI(azure_endpoint=endpoint, api_key=key, api_version="2024-02-01")
    return client, model


def complete(prompt: str) -> str:
    """Send prompt to primary vLLM; fall back to Ollama then Azure on failure."""
    try:
        client, model = _primary_client()
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
            max_tokens=4096,
        )
        content = _strip_thinking(resp.choices[0].message.content or "")
        if not content:
            raise ValueError("Primary LLM returned empty content")
        return content
    except Exception as e:
        print(f"Primary LLM failed ({e}), using Ollama fallback...")

    try:
        client, model = _ollama_client()
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
            max_tokens=4096,
        )
        content = _strip_thinking(resp.choices[0].message.content or "")
        if not content:
            raise ValueError("Ollama returned empty content")
        return content
    except Exception as e:
        print(f"Ollama fallback failed ({e}), using Azure fallback...")

    client, model = _azure_client()
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
    )
    content = _strip_thinking(resp.choices[0].message.content or "")
    if not content:
        raise ValueError("Azure LLM returned empty content")
    return content
