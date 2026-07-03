"""Model providers for Qwen Tris Recall.

OfflineProvider makes the scaffold runnable before Qwen Cloud credits land.
QwenCloudProvider is intentionally thin: set the API endpoint/key later without
changing the memory architecture.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
import os
import urllib.request

from .alibaba_qwen_cloud_client import (
    ALIBABA_QWEN_COMPATIBLE_BASE,
    DEFAULT_QWEN_MODEL,
    qwen_cloud_chat_completions_endpoint,
)


class ProviderError(RuntimeError):
    """Raised when a model provider cannot complete a request."""


@dataclass
class OfflineProvider:
    """Deterministic local provider for scaffold and A/B harness checks."""

    name: str = "offline-deterministic"

    def complete(self, prompt: str) -> str:
        if "BASELINE CONDITION A" in prompt:
            return (
                "Offline baseline response. No persistent memory was retrieved; "
                "answering from the visible prompt only."
            )
        signals = []
        lower = prompt.lower()
        for marker in ("correction", "next gate", "stale", "evidence", "stable-state"):
            if marker in lower:
                signals.append(marker)
        signal_text = ", ".join(signals) if signals else "no recalled signal"
        return (
            "Offline Qwen Tris Recall response. "
            f"Recovered signals: {signal_text}. "
            "Decision: preserve the active stable-state packet, cite retrieved memory, "
            "suppress stale memory, and continue from the current gate."
        )


@dataclass
class OllamaProvider:
    """Local Ollama provider for real Qwen/Nemotron chat routes."""

    model: str
    name: str = "ollama-local"
    api_base: str = "http://127.0.0.1:11434"
    timeout: float = 180.0

    def complete(self, prompt: str) -> str:
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are Qwen Tris Recall Memory AI Expert Partner. "
                        "Use the stable-state packet, retrieved memory, and retrieved RAG evidence. "
                        "Be direct, operational, and honest about runtime boundaries. "
                        "When a pinned target memory is present, use it as the primary source for exact facts. "
                        "If recall factors are provided, copy them verbatim before interpreting them."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
            "stream": False,
            "options": {"temperature": 0.0},
        }
        request = urllib.request.Request(
            f"{self.api_base.rstrip('/')}/api/chat",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(request, timeout=self.timeout) as response:
            data = json.loads(response.read().decode("utf-8", errors="replace"))
        try:
            return str(data["message"]["content"]).strip()
        except (KeyError, TypeError) as exc:
            raise ProviderError(f"Unexpected Ollama response shape: {data}") from exc


@dataclass
class QwenCloudProvider:
    """Qwen Cloud adapter placeholder.

    Expected environment after credits/API access:

    - QWEN_API_KEY
    - QWEN_API_BASE, optional
    - QWEN_MODEL, optional
    """

    api_key: str | None = None
    api_base: str = ALIBABA_QWEN_COMPATIBLE_BASE
    model: str = DEFAULT_QWEN_MODEL
    timeout: float = 90.0

    @classmethod
    def from_env(cls) -> "QwenCloudProvider":
        return cls(
            api_key=os.getenv("QWEN_API_KEY"),
            api_base=os.getenv("QWEN_API_BASE", cls.api_base),
            model=os.getenv("QWEN_MODEL", cls.model),
        )

    def complete(self, prompt: str) -> str:
        if not self.api_key:
            raise ProviderError("QWEN_API_KEY is not set; run OfflineProvider until credits/API key land.")
        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are Qwen inside Qwen Tris Recall Memory AI Expert Partner. "
                        "Follow the stable-state packet. When a pinned target memory is present, "
                        "use it as the primary source for exact facts. If recall factors are provided, "
                        "copy them verbatim before interpreting them."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.0,
        }
        endpoint = qwen_cloud_chat_completions_endpoint(self.api_base)
        request = urllib.request.Request(
            endpoint,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        with urllib.request.urlopen(request, timeout=self.timeout) as response:
            data = json.loads(response.read().decode("utf-8", errors="replace"))
        try:
            return str(data["choices"][0]["message"]["content"]).strip()
        except (KeyError, IndexError, TypeError) as exc:
            raise ProviderError(f"Unexpected Qwen response shape: {data}") from exc
