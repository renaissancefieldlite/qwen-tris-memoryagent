"""Alibaba Cloud / Qwen Cloud API proof client.

This file exists so judges can inspect the exact code path that connects the
Qwen Tris MemoryAgent backend to Alibaba Cloud Model Studio / Qwen Cloud.

No API keys are stored here. Set QWEN_API_KEY in the runtime environment.
"""

from __future__ import annotations

import json
import os
from typing import Any
import urllib.request


ALIBABA_QWEN_COMPATIBLE_BASE = "https://dashscope-intl.aliyuncs.com/compatible-mode/v1"
DEFAULT_QWEN_MODEL = "qwen-plus"


class QwenCloudAPIError(RuntimeError):
    """Raised when the Alibaba Cloud Qwen API route fails."""


def qwen_cloud_chat_completions_endpoint(api_base: str | None = None) -> str:
    """Return the Alibaba/Qwen OpenAI-compatible chat completions endpoint."""

    endpoint = (api_base or os.getenv("QWEN_API_BASE") or ALIBABA_QWEN_COMPATIBLE_BASE).rstrip("/")
    if not endpoint.endswith("/chat/completions"):
        endpoint = f"{endpoint}/chat/completions"
    return endpoint


def build_qwen_cloud_payload(
    prompt: str,
    *,
    model: str | None = None,
    system: str | None = None,
    temperature: float = 0.0,
) -> dict[str, Any]:
    """Build a public-safe Qwen Cloud chat payload for the MemoryAgent backend."""

    return {
        "model": model or os.getenv("QWEN_MODEL") or DEFAULT_QWEN_MODEL,
        "messages": [
            {
                "role": "system",
                "content": system
                or (
                    "You are Qwen inside Qwen Tris Recall Memory AI Expert Partner. "
                    "Use retrieved memory and source evidence. Stay concise, cite boundaries, "
                    "and do not claim unsupported live actions."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": temperature,
    }


def complete_with_qwen_cloud(
    prompt: str,
    *,
    api_key: str | None = None,
    api_base: str | None = None,
    model: str | None = None,
    timeout: float = 90.0,
) -> str:
    """Call Alibaba Cloud Qwen using the OpenAI-compatible endpoint."""

    key = api_key or os.getenv("QWEN_API_KEY")
    if not key:
        raise QwenCloudAPIError("QWEN_API_KEY is not set.")

    payload = build_qwen_cloud_payload(prompt, model=model)
    request = urllib.request.Request(
        qwen_cloud_chat_completions_endpoint(api_base),
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        data = json.loads(response.read().decode("utf-8", errors="replace"))
    try:
        return str(data["choices"][0]["message"]["content"]).strip()
    except (KeyError, IndexError, TypeError) as exc:
        raise QwenCloudAPIError(f"Unexpected Qwen Cloud response shape: {data}") from exc


if __name__ == "__main__":
    print(
        complete_with_qwen_cloud(
            "Return one sentence confirming that the Qwen Cloud MemoryAgent backend route is live."
        )
    )
