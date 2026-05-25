"""LLM client: primary vLLM endpoint with Azure OpenAI fallback."""

import os

from openai import AzureOpenAI, OpenAI


def _primary_client():
    endpoint = os.environ["VLLM_ENDPOINT"]
    model = os.environ.get("VLLM_MODEL", "")
    client = OpenAI(base_url=endpoint, api_key="dummy")
    return client, model


def _azure_client():
    endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
    key = os.environ["AZURE_OPENAI_KEY"]
    model = os.environ["AZURE_OPENAI_MODEL"]
    client = AzureOpenAI(azure_endpoint=endpoint, api_key=key, api_version="2024-02-01")
    return client, model


def complete(prompt: str) -> str:
    """Send prompt to primary vLLM; fall back to Azure on any failure."""
    try:
        client, model = _primary_client()
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
        )
        return resp.choices[0].message.content
    except Exception as e:
        print(f"Primary LLM failed ({e}), using Azure fallback...")
        client, model = _azure_client()
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
        )
        return resp.choices[0].message.content
