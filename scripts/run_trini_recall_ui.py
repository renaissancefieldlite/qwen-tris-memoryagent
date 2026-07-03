#!/usr/bin/env python3
"""Run the Qwen Tris Recall Memory AI Expert Partner local UI."""

from __future__ import annotations

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import argparse
import base64
import hashlib
from html.parser import HTMLParser
import importlib.util
import json
import mimetypes
import os
from pathlib import Path
import re
import socket
import sys
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
STATIC = ROOT / "static" / "trini_recall"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from qwen_agent_buildout.trini_recall import MemoryStore, OllamaProvider, QwenCloudProvider
from qwen_agent_buildout.trini_recall.bootstrap import build_offline_agent, seed_default_memories
from qwen_agent_buildout.trini_recall.evaluation import score_response


DEFAULT_DB = Path(os.getenv("TRINI_RECALL_DB_PATH", "/tmp/trini_recall_chat_memory.sqlite3"))
DEFAULT_JSONL = Path(os.getenv("TRINI_RECALL_JSONL_PATH", "/tmp/trini_recall_chat_memory.jsonl"))
OLLAMA_BASE = os.getenv("TRINI_OLLAMA_BASE", "http://127.0.0.1:11434")
LOCAL_QWEN_MODEL = os.getenv("TRINI_QWEN_MODEL", "qwen2.5:3b")
LOCAL_NEMOTRON_MODEL = os.getenv("TRINI_NEMOTRON_MODEL", "hf.co/nvidia/NVIDIA-Nemotron-3-Nano-4B-GGUF:Q4_K_M")
HOME_NODE_URL = os.getenv("TRINI_HOME_NODE_URL", "http://127.0.0.1:7863")
AUDIO_DIR = Path(os.getenv("TRINI_RECALL_AUDIO_DIR", "/tmp/trini_recall_audio"))
MAX_FETCH_BYTES = 350_000
MAX_EVIDENCE_BODY_CHARS = 20_000


def find_free_port(preferred: int | None = None) -> int:
    candidates: list[int] = []
    if preferred:
        candidates.append(preferred)
    candidates.extend(range(9471, 9510))
    candidates.extend(range(12080, 12140))
    candidates.extend(range(18080, 18140))
    for port in candidates:
        with socket.socket() as sock:
            try:
                sock.bind(("127.0.0.1", port))
            except OSError:
                continue
            return port
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def json_response(handler: SimpleHTTPRequestHandler, payload: object, status: int = 200) -> None:
    body = json.dumps(payload, indent=2).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


def read_json(handler: SimpleHTTPRequestHandler) -> dict[str, object]:
    length = int(handler.headers.get("Content-Length", "0") or 0)
    if not length:
        return {}
    body = handler.rfile.read(length).decode("utf-8", errors="replace")
    return json.loads(body or "{}")


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title_parts: list[str] = []
        self.text_parts: list[str] = []
        self._in_title = False
        self._skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "noscript", "svg"}:
            self._skip_depth += 1
        if tag == "title":
            self._in_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript", "svg"} and self._skip_depth:
            self._skip_depth -= 1
        if tag == "title":
            self._in_title = False

    def handle_data(self, data: str) -> None:
        clean = data.strip()
        if not clean or self._skip_depth:
            return
        if self._in_title:
            self.title_parts.append(clean)
        else:
            self.text_parts.append(clean)

    @property
    def title(self) -> str:
        return normalize_text(" ".join(self.title_parts))[:240]

    @property
    def body(self) -> str:
        return normalize_text(" ".join(self.text_parts))


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def append_jsonl(path: Path, event_type: str, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    event = {"created_at": current_utc(), "event_type": event_type, "payload": payload}
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, sort_keys=True) + "\n")


def read_jsonl_tail(path: Path, limit: int = 80) -> list[dict[str, object]]:
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()[-limit:]
    events: list[dict[str, object]] = []
    for line in lines:
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return events


def current_utc() -> str:
    from datetime import datetime, timezone

    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def fetch_source(url: str) -> dict[str, object]:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("web fetch requires an http or https URL")
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "QwenTrisRecallMemoryAIPartner/0.1 (+local-track1-demo)",
            "Accept": "text/html,text/plain,application/json;q=0.8,*/*;q=0.5",
        },
    )
    with urllib.request.urlopen(request, timeout=18) as response:
        content_type = response.headers.get("Content-Type", "")
        raw = response.read(MAX_FETCH_BYTES + 1)
        final_url = response.geturl()
    if len(raw) > MAX_FETCH_BYTES:
        raw = raw[:MAX_FETCH_BYTES]
    charset = "utf-8"
    match = re.search(r"charset=([^;\s]+)", content_type, flags=re.I)
    if match:
        charset = match.group(1).strip('"')
    text = raw.decode(charset, errors="replace")
    if "html" in content_type.lower() or "<html" in text[:1000].lower():
        parser = TextExtractor()
        parser.feed(text)
        title = parser.title or final_url
        body = parser.body
    else:
        title = final_url
        body = normalize_text(text)
    if not body:
        raise ValueError("web fetch returned no readable text")
    body = body[:MAX_EVIDENCE_BODY_CHARS]
    body_hash = hashlib.sha256(body.encode("utf-8")).hexdigest()
    doc_id = "web_" + hashlib.sha256(f"{final_url}:{body_hash}".encode("utf-8")).hexdigest()[:16]
    return {
        "id": doc_id,
        "title": str(title)[:240],
        "body": body,
        "source_ref": final_url,
        "body_hash": body_hash,
        "content_type": content_type,
        "bytes_read": len(raw),
    }


def ollama_models() -> list[str]:
    try:
        with urllib.request.urlopen(f"{OLLAMA_BASE.rstrip('/')}/api/tags", timeout=3) as response:
            data = json.loads(response.read().decode("utf-8", errors="replace"))
        return [str(item.get("name") or "") for item in data.get("models", []) if item.get("name")]
    except Exception:
        return []


def home_node_online() -> bool:
    for path in ("/health", "/api/health", "/"):
        try:
            with urllib.request.urlopen(f"{HOME_NODE_URL.rstrip('/')}{path}", timeout=1.5) as response:
                return 200 <= getattr(response, "status", 200) < 500
        except Exception:
            continue
    return False


def langchain_status() -> dict[str, object]:
    modules = {
        "langchain": bool(importlib.util.find_spec("langchain")),
        "langchain_core": bool(importlib.util.find_spec("langchain_core")),
        "langchain_community": bool(importlib.util.find_spec("langchain_community")),
        "langchain_text_splitters": bool(importlib.util.find_spec("langchain_text_splitters")),
    }
    online = modules["langchain_core"] and modules["langchain_text_splitters"]
    return {
        "online": online,
        "modules": modules,
        "mode": "LangChain Document/TextSplitter over SQLite FTS evidence store" if online else "SQLite/FTS fallback",
    }


def audio_status() -> dict[str, object]:
    return {
        "browser_voice": True,
        "browser_media_recorder": True,
        "home_node_online": home_node_online(),
        "home_node_url": HOME_NODE_URL,
        "server_transcription": bool(importlib.util.find_spec("faster_whisper") and importlib.util.find_spec("av")),
        "storage_dir": str(AUDIO_DIR),
    }


def provider_status() -> dict[str, object]:
    models = ollama_models()
    return {
        "qwen_cloud": {
            "online": bool(os.getenv("QWEN_API_KEY")),
            "model": os.getenv("QWEN_MODEL", "qwen-plus"),
            "route": "Qwen Cloud API",
        },
        "qwen_local": {
            "online": LOCAL_QWEN_MODEL in models,
            "model": LOCAL_QWEN_MODEL,
            "route": OLLAMA_BASE,
        },
        "nemotron_local": {
            "online": LOCAL_NEMOTRON_MODEL in models,
            "model": LOCAL_NEMOTRON_MODEL,
            "route": OLLAMA_BASE,
        },
        "nemoclaw": {
            "online": False,
            "model": "not connected",
            "route": "no verified NemoClaw API mounted in this app",
        },
        "langchain_rag": langchain_status(),
        "audio": audio_status(),
        "ollama_models": models,
    }


def select_provider(route: str) -> object:
    status = provider_status()
    normalized = route.strip().lower()
    if normalized == "qwen_cloud":
        if not status["qwen_cloud"]["online"]:
            raise ValueError("Qwen Cloud is not connected: QWEN_API_KEY is not set.")
        return QwenCloudProvider.from_env()
    if normalized == "nemotron":
        if not status["nemotron_local"]["online"]:
            raise ValueError(f"Nemotron is not available in Ollama as {LOCAL_NEMOTRON_MODEL}.")
        return OllamaProvider(model=LOCAL_NEMOTRON_MODEL, name="ollama-nemotron", api_base=OLLAMA_BASE)
    if normalized == "qwen":
        if not status["qwen_local"]["online"]:
            raise ValueError(f"Local Qwen is not available in Ollama as {LOCAL_QWEN_MODEL}.")
        return OllamaProvider(model=LOCAL_QWEN_MODEL, name="ollama-qwen", api_base=OLLAMA_BASE)
    if normalized == "auto":
        if status["qwen_local"]["online"]:
            return OllamaProvider(model=LOCAL_QWEN_MODEL, name="ollama-qwen", api_base=OLLAMA_BASE)
        if status["nemotron_local"]["online"]:
            return OllamaProvider(model=LOCAL_NEMOTRON_MODEL, name="ollama-nemotron", api_base=OLLAMA_BASE)
        if status["qwen_cloud"]["online"]:
            return QwenCloudProvider.from_env()
    raise ValueError("No real provider route is connected. Start Ollama Qwen/Nemotron or set QWEN_API_KEY.")


def init_chat_db(store: MemoryStore) -> None:
    with store.connect() as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS chats (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS chat_messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id TEXT NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                provider TEXT NOT NULL DEFAULT '',
                route TEXT NOT NULL DEFAULT '',
                created_at TEXT NOT NULL
            );
            """
        )


def list_chats(store: MemoryStore) -> list[dict[str, object]]:
    with store.connect() as conn:
        rows = conn.execute(
            """
            SELECT c.id, c.title, c.created_at, c.updated_at, COUNT(m.id) AS message_count
            FROM chats c
            LEFT JOIN chat_messages m ON m.chat_id = c.id
            GROUP BY c.id
            ORDER BY c.updated_at DESC
            """
        ).fetchall()
    return [dict(row) for row in rows]


def chat_messages(store: MemoryStore, chat_id: str) -> list[dict[str, object]]:
    with store.connect() as conn:
        rows = conn.execute(
            """
            SELECT role, content, provider, route, created_at
            FROM chat_messages
            WHERE chat_id = ?
            ORDER BY id
            """,
            (chat_id,),
        ).fetchall()
    return [dict(row) for row in rows]


def ensure_chat(store: MemoryStore, chat_id: str | None, title_seed: str) -> str:
    now = current_utc()
    if chat_id:
        with store.connect() as conn:
            row = conn.execute("SELECT id FROM chats WHERE id = ?", (chat_id,)).fetchone()
        if row:
            return chat_id
    new_id = "chat_" + hashlib.sha256(f"{now}:{title_seed}".encode("utf-8")).hexdigest()[:14]
    title = normalize_text(title_seed)[:54] or "New Qwen Tris chat"
    with store.connect() as conn:
        conn.execute(
            "INSERT INTO chats(id, title, created_at, updated_at) VALUES (?, ?, ?, ?)",
            (new_id, title, now, now),
        )
    return new_id


def add_chat_message(
    store: MemoryStore,
    chat_id: str,
    role: str,
    content: str,
    *,
    provider: str = "",
    route: str = "",
) -> None:
    now = current_utc()
    with store.connect() as conn:
        conn.execute(
            """
            INSERT INTO chat_messages(chat_id, role, content, provider, route, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (chat_id, role, content, provider, route, now),
        )
        conn.execute("UPDATE chats SET updated_at = ? WHERE id = ?", (now, chat_id))


def delete_chat(store: MemoryStore, chat_id: str) -> None:
    with store.connect() as conn:
        conn.execute("DELETE FROM chat_messages WHERE chat_id = ?", (chat_id,))
        conn.execute("DELETE FROM chats WHERE id = ?", (chat_id,))


def maybe_capture_memory(store: MemoryStore, message: str, chat_id: str) -> str | None:
    lower = message.lower()
    if not any(marker in lower for marker in ("remember", "correction", "preference", "next gate", "lock this")):
        return None
    memory_id = "chat_memory_" + hashlib.sha256(f"{chat_id}:{message}".encode("utf-8")).hexdigest()[:12]
    kind = "correction" if "correction" in lower else "next_gate" if "next gate" in lower else "preference"
    store.add_memory(
        id=memory_id,
        kind=kind,
        content=message,
        source_ref=f"chat/{chat_id}",
        tags=("chat", "captured"),
        privacy_class="internal",
        reason="captured from chat instruction",
    )
    return memory_id


def langchain_evidence_hits(store: MemoryStore, query: str, limit: int = 4):
    """Use LangChain document wrappers when installed, backed by local SQLite/FTS."""

    hits = store.search_evidence(query, limit=limit)
    if not langchain_status()["online"]:
        return hits, "sqlite_fts"
    try:
        from langchain_core.documents import Document
        from langchain_text_splitters import RecursiveCharacterTextSplitter

        docs = [
            Document(
                page_content=hit.doc.body,
                metadata={
                    "id": hit.doc.id,
                    "title": hit.doc.title,
                    "source_ref": hit.doc.source_ref,
                    "reason": hit.reason,
                },
            )
            for hit in hits
        ]
        splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=120)
        chunks = splitter.split_documents(docs)
        if not chunks:
            return hits, "langchain_empty"
        # SQLite FTS chooses documents; LangChain normalizes chunks for prompt packing.
        kept_ids = {chunk.metadata.get("id") for chunk in chunks[:limit]}
        ranked = [hit for hit in hits if hit.doc.id in kept_ids]
        return ranked or hits, "langchain_sqlite_fts"
    except Exception:
        return hits, "sqlite_fts_langchain_error"


def save_audio_data_url(data_url: str) -> dict[str, object] | None:
    if not data_url:
        return None
    match = re.match(r"^data:([^;,]+)?(?:;codecs=[^;,]+)?;base64,(.+)$", data_url, flags=re.I | re.S)
    if not match:
        raise ValueError("audio payload must be a data URL")
    mime = match.group(1) or "audio/webm"
    payload = base64.b64decode(match.group(2), validate=False)
    if len(payload) > 24 * 1024 * 1024:
        raise ValueError("audio payload is larger than 24MB")
    suffix = ".webm" if "webm" in mime else ".wav" if "wav" in mime else ".audio"
    digest = hashlib.sha256(payload).hexdigest()
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    path = AUDIO_DIR / f"{digest[:18]}{suffix}"
    path.write_bytes(payload)
    return {"path": str(path), "mime": mime, "sha256": digest, "bytes": len(payload)}


def transcribe_audio_if_available(audio_path: str) -> str:
    if not (importlib.util.find_spec("faster_whisper") and importlib.util.find_spec("av")):
        return ""
    try:
        from faster_whisper import WhisperModel

        model = WhisperModel("base", device="cpu", compute_type="int8")
        segments, _ = model.transcribe(audio_path, vad_filter=True)
        return " ".join(segment.text.strip() for segment in segments if segment.text.strip()).strip()
    except Exception as exc:
        return f"[Audio transcription error: {exc}]"


def memory_payload(store: MemoryStore, jsonl_path: Path) -> dict[str, object]:
    return {
        "db_path": str(store.db_path),
        "jsonl_path": str(jsonl_path),
        "items": [
            {
                "id": item.id,
                "kind": item.kind,
                "content": item.content,
                "source_ref": item.source_ref,
                "privacy_class": item.privacy_class,
                "confidence": item.confidence,
                "status": item.status,
                "tags": list(item.tags),
                "created_at": item.created_at,
                "updated_at": item.updated_at,
                "supersedes_id": item.supersedes_id,
            }
            for item in store.list_items()
        ],
        "evidence_docs": [
            {
                "id": doc.id,
                "title": doc.title,
                "body": doc.body[:900],
                "source_ref": doc.source_ref,
                "body_hash": doc.body_hash,
                "privacy_class": doc.privacy_class,
                "created_at": doc.created_at,
                "updated_at": doc.updated_at,
                "metadata": doc.metadata,
            }
            for doc in store.list_evidence()
        ],
        "retrieval_events": store.retrieval_events()[-80:],
        "evidence_retrieval_events": store.evidence_retrieval_events()[-80:],
        "jsonl_events": read_jsonl_tail(jsonl_path),
    }


class TriniRecallUIHandler(SimpleHTTPRequestHandler):
    store: MemoryStore
    jsonl_path: Path

    def __init__(self, *args: object, **kwargs: object) -> None:
        super().__init__(*args, directory=str(STATIC), **kwargs)

    def log_message(self, format: str, *args: object) -> None:  # noqa: A002
        sys.stderr.write("[trini-recall-ui] " + format % args + "\n")

    def do_GET(self) -> None:  # noqa: N802
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/api/state":
            json_response(
                self,
                {
                    "ok": True,
                    "app": "Qwen Tris Recall Memory AI Expert Partner",
                    "mode": "chat partner",
                    "providers": provider_status(),
                    **memory_payload(self.store, self.jsonl_path),
                },
            )
            return
        if parsed.path == "/api/health":
            status = provider_status()
            json_response(
                self,
                {
                    "ok": True,
                    "providers": status,
                    "memory_count": len(self.store.list_items()),
                    "evidence_count": len(self.store.list_evidence()),
                    "chats": len(list_chats(self.store)),
                },
            )
            return
        if parsed.path == "/api/chats":
            json_response(self, {"ok": True, "chats": list_chats(self.store)})
            return
        if parsed.path == "/api/messages":
            query = urllib.parse.parse_qs(parsed.query)
            chat_id = str((query.get("chat_id") or [""])[0])
            json_response(self, {"ok": True, "messages": chat_messages(self.store, chat_id) if chat_id else []})
            return
        if parsed.path == "/":
            self.path = "/index.html"
        return super().do_GET()

    def do_POST(self) -> None:  # noqa: N802
        parsed = urllib.parse.urlparse(self.path)
        try:
            if parsed.path == "/api/chat":
                payload = read_json(self)
                message = str(payload.get("message") or "").strip()
                route = str(payload.get("route") or "auto").strip() or "auto"
                mic_audio_data = str(payload.get("mic_audio_data") or "").strip()
                chat_id_in = str(payload.get("chat_id") or "").strip() or None
                audio_receipt = save_audio_data_url(mic_audio_data) if mic_audio_data else None
                transcript = transcribe_audio_if_available(str(audio_receipt["path"])) if audio_receipt else ""
                if transcript and not transcript.startswith("["):
                    message = f"{message}\n\n[Voice Input]\n{transcript}".strip()
                elif audio_receipt and not message:
                    message = "[Audio capture attached. Server transcription is offline.]"
                if not message:
                    json_response(self, {"ok": False, "error": "message is required"}, status=400)
                    return
                provider = select_provider(route)
                chat_id = ensure_chat(self.store, chat_id_in, message)
                prior = chat_messages(self.store, chat_id)[-8:]
                history = "\n".join(f"{row['role']}: {row['content']}" for row in prior)
                add_chat_message(self.store, chat_id, "user", message)
                captured_memory_id = maybe_capture_memory(self.store, message, chat_id)
                agent = build_offline_agent(self.store)
                agent.provider = provider
                prompt_message = (
                    f"Chat session: {chat_id}\n"
                    f"Recent chat history:\n{history or '[new chat]'}\n\n"
                    f"User message:\n{message}"
                )
                evidence_hits, rag_mode = langchain_evidence_hits(self.store, prompt_message, limit=4)
                result = agent.answer(prompt_message, architecture_on=True, evidence_hits=evidence_hits, rag_mode=rag_mode)
                provider_name = result.provider_name
                provider_route = getattr(provider, "model", provider_name)
                add_chat_message(
                    self.store,
                    chat_id,
                    "assistant",
                    result.response,
                    provider=provider_name,
                    route=str(provider_route),
                )
                append_jsonl(
                    self.jsonl_path,
                    "chat_turn",
                    {
                        "chat_id": chat_id,
                        "route": route,
                        "provider": provider_name,
                        "model": str(provider_route),
                        "rag_mode": rag_mode,
                        "memory_count": len(result.retrievals),
                        "evidence_count": len(result.evidence_hits),
                        "captured_memory_id": captured_memory_id,
                        "audio": audio_receipt,
                        "transcript_present": bool(transcript),
                    },
                )
                json_response(
                    self,
                    {
                        "ok": True,
                        "chat_id": chat_id,
                        "response": result.response,
                        "provider": provider_name,
                        "model": str(provider_route),
                        "rag_mode": rag_mode,
                        "captured_memory_id": captured_memory_id,
                        "audio": audio_receipt,
                        "transcript": transcript,
                        "retrievals": [
                            {
                                "id": retrieval.item.id,
                                "kind": retrieval.item.kind,
                                "content": retrieval.item.content,
                                "reason": retrieval.reason,
                                "source_ref": retrieval.item.source_ref,
                            }
                            for retrieval in result.retrievals
                        ],
                        "evidence": [
                            {
                                "id": hit.doc.id,
                                "title": hit.doc.title,
                                "body": hit.doc.body[:700],
                                "reason": hit.reason,
                                "source_ref": hit.doc.source_ref,
                            }
                            for hit in result.evidence_hits
                        ],
                        "messages": chat_messages(self.store, chat_id),
                        "chats": list_chats(self.store),
                        "state": memory_payload(self.store, self.jsonl_path),
                    },
                )
                return
            if parsed.path == "/api/chats/delete":
                payload = read_json(self)
                chat_id = str(payload.get("chat_id") or "").strip()
                if not chat_id:
                    json_response(self, {"ok": False, "error": "chat_id is required"}, status=400)
                    return
                delete_chat(self.store, chat_id)
                append_jsonl(self.jsonl_path, "chat_deleted", {"chat_id": chat_id})
                json_response(self, {"ok": True, "chats": list_chats(self.store)})
                return
            if parsed.path == "/api/run":
                payload = read_json(self)
                message = str(payload.get("message") or "").strip()
                if not message:
                    json_response(self, {"ok": False, "error": "message is required"}, status=400)
                    return
                agent = build_offline_agent(self.store)
                baseline = agent.answer(message, architecture_on=False)
                architecture_on = agent.answer(message, architecture_on=True)
                append_jsonl(
                    self.jsonl_path,
                    "agent_run",
                    {
                        "message": message,
                        "condition_a_retrieval_count": len(baseline.retrievals),
                        "condition_b_retrieval_count": len(architecture_on.retrievals),
                        "condition_b_evidence_count": len(architecture_on.evidence_hits),
                    },
                )
                json_response(
                    self,
                    {
                        "ok": True,
                        "message": message,
                        "condition_a": {
                            "provider": baseline.provider_name,
                            "response": baseline.response,
                            "score": score_response(baseline.response).__dict__,
                            "retrieval_count": len(baseline.retrievals),
                            "prompt": baseline.prompt,
                        },
                        "condition_b": {
                            "provider": architecture_on.provider_name,
                            "response": architecture_on.response,
                            "score": score_response(architecture_on.response).__dict__,
                            "retrieval_count": len(architecture_on.retrievals),
                            "evidence_count": len(architecture_on.evidence_hits),
                            "prompt": architecture_on.prompt,
                            "stable_state_packet": architecture_on.packet.render(),
                            "retrievals": [
                                {
                                    "id": retrieval.item.id,
                                    "kind": retrieval.item.kind,
                                    "content": retrieval.item.content,
                                    "reason": retrieval.reason,
                                    "source_ref": retrieval.item.source_ref,
                                    "token_estimate": retrieval.token_estimate,
                                }
                                for retrieval in architecture_on.retrievals
                            ],
                            "evidence_hits": [
                                {
                                    "id": hit.doc.id,
                                    "title": hit.doc.title,
                                    "body": hit.doc.body[:900],
                                    "reason": hit.reason,
                                    "source_ref": hit.doc.source_ref,
                                    "token_estimate": hit.token_estimate,
                                }
                                for hit in architecture_on.evidence_hits
                            ],
                        },
                        "state": memory_payload(self.store, self.jsonl_path),
                    },
                )
                return
            if parsed.path == "/api/memory":
                payload = read_json(self)
                memory_id = str(payload.get("id") or "").strip()
                content = str(payload.get("content") or "").strip()
                if not memory_id or not content:
                    json_response(self, {"ok": False, "error": "id and content are required"}, status=400)
                    return
                tags = [tag.strip() for tag in str(payload.get("tags") or "").split(",") if tag.strip()]
                item = self.store.add_memory(
                    id=memory_id,
                    kind=str(payload.get("kind") or "preference").strip() or "preference",
                    content=content,
                    source_ref=str(payload.get("source_ref") or "ui/manual").strip() or "ui/manual",
                    tags=tags,
                    privacy_class=str(payload.get("privacy_class") or "internal").strip() or "internal",
                    reason="added from UI",
                )
                append_jsonl(
                    self.jsonl_path,
                    "memory_added",
                    {"id": item.id, "kind": item.kind, "source_ref": item.source_ref, "tags": list(item.tags)},
                )
                json_response(self, {"ok": True, "item": item.__dict__, "state": memory_payload(self.store, self.jsonl_path)})
                return
            if parsed.path == "/api/web-fetch":
                payload = read_json(self)
                url = str(payload.get("url") or "").strip()
                if not url:
                    json_response(self, {"ok": False, "error": "url is required"}, status=400)
                    return
                fetched = fetch_source(url)
                doc = self.store.add_evidence_doc(
                    id=str(fetched["id"]),
                    title=str(fetched["title"]),
                    body=str(fetched["body"]),
                    source_ref=str(fetched["source_ref"]),
                    body_hash=str(fetched["body_hash"]),
                    privacy_class="internal",
                    metadata={
                        "content_type": fetched["content_type"],
                        "bytes_read": fetched["bytes_read"],
                        "ingest": "ui_web_fetch",
                    },
                    reason="web fetch from UI",
                )
                excerpt = str(fetched["body"])[:700]
                memory_id = "source_" + doc.id
                memory = self.store.add_memory(
                    id=memory_id,
                    kind="evidence",
                    content=f"Fetched source '{doc.title}' from {doc.source_ref}. Excerpt: {excerpt}",
                    source_ref=doc.source_ref,
                    tags=("web", "rag", "source"),
                    privacy_class="internal",
                    reason="web fetch summary memory",
                )
                append_jsonl(
                    self.jsonl_path,
                    "web_fetch_added",
                    {
                        "evidence_id": doc.id,
                        "memory_id": memory.id,
                        "title": doc.title,
                        "source_ref": doc.source_ref,
                        "body_hash": doc.body_hash,
                    },
                )
                json_response(
                    self,
                    {
                        "ok": True,
                        "doc": {
                            "id": doc.id,
                            "title": doc.title,
                            "body": doc.body[:900],
                            "source_ref": doc.source_ref,
                            "body_hash": doc.body_hash,
                        },
                        "memory_id": memory.id,
                        "state": memory_payload(self.store, self.jsonl_path),
                    },
                )
                return
            if parsed.path == "/api/retire":
                payload = read_json(self)
                memory_id = str(payload.get("id") or "").strip()
                reason = str(payload.get("reason") or "retired from UI").strip()
                if not memory_id:
                    json_response(self, {"ok": False, "error": "id is required"}, status=400)
                    return
                self.store.retire_memory(memory_id, reason)
                append_jsonl(self.jsonl_path, "memory_retired", {"id": memory_id, "reason": reason})
                json_response(self, {"ok": True, "state": memory_payload(self.store, self.jsonl_path)})
                return
            json_response(self, {"ok": False, "error": f"unknown endpoint {parsed.path}"}, status=404)
        except Exception as exc:  # noqa: BLE001 - UI should surface errors.
            json_response(self, {"ok": False, "error": str(exc)}, status=500)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Qwen Tris Recall Memory AI Expert Partner UI")
    parser.add_argument("--port", default="auto", help="Port number or auto")
    parser.add_argument("--host", default=os.getenv("HOST", "127.0.0.1"), help="Bind host, use 0.0.0.0 for cloud/container deployment")
    parser.add_argument("--db", default=str(DEFAULT_DB), help="SQLite memory DB path")
    parser.add_argument("--jsonl", default=str(DEFAULT_JSONL), help="JSONL event ledger path")
    parser.add_argument("--open", action="store_true", help="Open the UI in the default browser")
    args = parser.parse_args()

    port_arg = os.getenv("PORT", str(args.port))
    preferred = None if str(port_arg).lower() == "auto" else int(port_arg)
    port = find_free_port(preferred)
    store = MemoryStore(args.db)
    jsonl_path = Path(args.jsonl)
    init_chat_db(store)
    seed_default_memories(store)
    TriniRecallUIHandler.store = store
    TriniRecallUIHandler.jsonl_path = jsonl_path
    append_jsonl(
        jsonl_path,
        "ui_started",
        {
            "db_path": str(store.db_path),
            "port": port,
            "mode": "chat partner",
            "app": "Qwen Tris Recall Memory AI Expert Partner",
        },
    )

    mimetypes.add_type("text/javascript", ".js")
    server = ThreadingHTTPServer((str(args.host), port), TriniRecallUIHandler)
    url_host = "127.0.0.1" if str(args.host) in {"0.0.0.0", "::"} else str(args.host)
    url = f"http://{url_host}:{port}"
    print(f"Qwen Tris Recall Memory AI Expert Partner UI: {url}")
    print(f"Memory DB: {store.db_path}")
    print(f"JSONL ledger: {jsonl_path}")
    if args.open:
        os.system(f"/usr/bin/open {url!r}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nQwen Tris Recall UI stopped.")
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
