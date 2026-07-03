"""SQLite/FTS memory store for Trini Recall.

The store is deliberately local-first. It can run before Qwen Cloud credits
land, then feed the same retrieval packet to the Qwen provider later.
"""

from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timezone
import json
import re
import sqlite3
from pathlib import Path
from typing import Any, Iterable, Iterator


ACTIVE = "active"
SUPERSEDED = "superseded"
RETIRED = "retired"
BLOCKED = "blocked"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def tokenize(text: str) -> list[str]:
    tokens = re.findall(r"[A-Za-z0-9]{3,}", text.lower())
    seen: set[str] = set()
    unique: list[str] = []
    for token in tokens:
        if token not in seen:
            seen.add(token)
            unique.append(token)
    return unique[:16]


@dataclass(frozen=True)
class MemoryItem:
    id: str
    kind: str
    content: str
    source_ref: str
    privacy_class: str
    confidence: float
    status: str
    tags: tuple[str, ...]
    created_at: str
    updated_at: str
    supersedes_id: str | None = None
    expires_at: str | None = None


@dataclass(frozen=True)
class Retrieval:
    item: MemoryItem
    reason: str
    score: float
    token_estimate: int


@dataclass(frozen=True)
class EvidenceDoc:
    id: str
    title: str
    body: str
    source_ref: str
    body_hash: str
    privacy_class: str
    created_at: str
    updated_at: str
    metadata: dict[str, Any]


@dataclass(frozen=True)
class EvidenceHit:
    doc: EvidenceDoc
    reason: str
    score: float
    token_estimate: int


class MemoryStore:
    """Persistent memory with explicit retrieval and forgetting ledgers."""

    def __init__(self, db_path: Path | str) -> None:
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    @contextmanager
    def connect(self) -> Iterator[sqlite3.Connection]:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
            conn.commit()
        finally:
            conn.close()

    def _init_db(self) -> None:
        with self.connect() as conn:
            conn.executescript(
                """
                CREATE TABLE IF NOT EXISTS memory_items (
                    id TEXT PRIMARY KEY,
                    kind TEXT NOT NULL,
                    content TEXT NOT NULL,
                    source_ref TEXT NOT NULL,
                    privacy_class TEXT NOT NULL,
                    confidence REAL NOT NULL,
                    status TEXT NOT NULL,
                    tags_json TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL,
                    supersedes_id TEXT,
                    expires_at TEXT
                );

                CREATE VIRTUAL TABLE IF NOT EXISTS memory_fts
                USING fts5(id UNINDEXED, kind, content, source_ref, tags);

                CREATE TABLE IF NOT EXISTS memory_events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    memory_id TEXT NOT NULL,
                    event_type TEXT NOT NULL,
                    reason TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    metadata_json TEXT NOT NULL DEFAULT '{}'
                );

                CREATE TABLE IF NOT EXISTS retrieval_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    query TEXT NOT NULL,
                    memory_id TEXT NOT NULL,
                    reason TEXT NOT NULL,
                    score REAL NOT NULL,
                    token_estimate INTEGER NOT NULL,
                    created_at TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS evidence_docs (
                    id TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    body TEXT NOT NULL,
                    source_ref TEXT NOT NULL,
                    body_hash TEXT NOT NULL,
                    privacy_class TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL,
                    metadata_json TEXT NOT NULL DEFAULT '{}'
                );

                CREATE VIRTUAL TABLE IF NOT EXISTS evidence_fts
                USING fts5(id UNINDEXED, title, body, source_ref);

                CREATE TABLE IF NOT EXISTS evidence_events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    evidence_id TEXT NOT NULL,
                    event_type TEXT NOT NULL,
                    reason TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    metadata_json TEXT NOT NULL DEFAULT '{}'
                );

                CREATE TABLE IF NOT EXISTS evidence_retrieval_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    query TEXT NOT NULL,
                    evidence_id TEXT NOT NULL,
                    reason TEXT NOT NULL,
                    score REAL NOT NULL,
                    token_estimate INTEGER NOT NULL,
                    created_at TEXT NOT NULL
                );
                """
            )

    def add_memory(
        self,
        *,
        id: str,
        kind: str,
        content: str,
        source_ref: str,
        tags: Iterable[str] = (),
        privacy_class: str = "internal",
        confidence: float = 1.0,
        supersedes_id: str | None = None,
        expires_at: str | None = None,
        reason: str = "created",
    ) -> MemoryItem:
        now = utc_now()
        tags_tuple = tuple(dict.fromkeys(tag.strip() for tag in tags if tag.strip()))
        item = MemoryItem(
            id=id,
            kind=kind,
            content=content.strip(),
            source_ref=source_ref,
            privacy_class=privacy_class,
            confidence=float(confidence),
            status=ACTIVE,
            tags=tags_tuple,
            created_at=now,
            updated_at=now,
            supersedes_id=supersedes_id,
            expires_at=expires_at,
        )
        with self.connect() as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO memory_items
                    (id, kind, content, source_ref, privacy_class, confidence,
                     status, tags_json, created_at, updated_at, supersedes_id,
                     expires_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    item.id,
                    item.kind,
                    item.content,
                    item.source_ref,
                    item.privacy_class,
                    item.confidence,
                    item.status,
                    json.dumps(item.tags),
                    item.created_at,
                    item.updated_at,
                    item.supersedes_id,
                    item.expires_at,
                ),
            )
            conn.execute("DELETE FROM memory_fts WHERE id = ?", (item.id,))
            conn.execute(
                "INSERT INTO memory_fts(id, kind, content, source_ref, tags) VALUES (?, ?, ?, ?, ?)",
                (item.id, item.kind, item.content, item.source_ref, " ".join(item.tags)),
            )
            conn.execute(
                """
                INSERT INTO memory_events(memory_id, event_type, reason, created_at, metadata_json)
                VALUES (?, ?, ?, ?, ?)
                """,
                (item.id, "created", reason, now, "{}"),
            )
            if supersedes_id:
                self._set_status(conn, supersedes_id, SUPERSEDED, f"superseded by {id}")
        return item

    def retire_memory(self, memory_id: str, reason: str, status: str = RETIRED) -> None:
        with self.connect() as conn:
            self._set_status(conn, memory_id, status, reason)

    def _set_status(self, conn: sqlite3.Connection, memory_id: str, status: str, reason: str) -> None:
        now = utc_now()
        conn.execute(
            "UPDATE memory_items SET status = ?, updated_at = ? WHERE id = ?",
            (status, now, memory_id),
        )
        conn.execute("DELETE FROM memory_fts WHERE id = ?", (memory_id,))
        conn.execute(
            """
            INSERT INTO memory_events(memory_id, event_type, reason, created_at, metadata_json)
            VALUES (?, ?, ?, ?, ?)
            """,
            (memory_id, status, reason, now, "{}"),
        )

    def retrieve(
        self,
        query: str,
        *,
        limit: int = 6,
        allowed_privacy: Iterable[str] = ("public", "internal"),
    ) -> list[Retrieval]:
        allowed = tuple(allowed_privacy)
        if not allowed:
            return []
        tokens = tokenize(query)
        rows: list[sqlite3.Row]
        with self.connect() as conn:
            if tokens:
                match = " OR ".join(tokens)
                try:
                    rows = conn.execute(
                        f"""
                        SELECT mi.*, bm25(memory_fts) AS rank
                        FROM memory_fts
                        JOIN memory_items mi ON mi.id = memory_fts.id
                        WHERE memory_fts MATCH ?
                          AND mi.status = ?
                          AND mi.privacy_class IN ({",".join("?" for _ in allowed)})
                        ORDER BY rank
                        LIMIT ?
                        """,
                        (match, ACTIVE, *allowed, limit),
                    ).fetchall()
                except sqlite3.OperationalError:
                    rows = self._like_search(conn, query, allowed, limit)
            else:
                rows = conn.execute(
                    f"""
                    SELECT *, 0.0 AS rank
                    FROM memory_items
                    WHERE status = ?
                      AND privacy_class IN ({",".join("?" for _ in allowed)})
                    ORDER BY updated_at DESC
                    LIMIT ?
                    """,
                    (ACTIVE, *allowed, limit),
                ).fetchall()

        retrievals = [self._retrieval_from_row(row, query) for row in rows]
        self._log_retrievals(query, retrievals)
        return retrievals

    def get_memory(
        self,
        memory_id: str,
        *,
        allowed_privacy: Iterable[str] = ("public", "internal"),
    ) -> MemoryItem | None:
        allowed = tuple(allowed_privacy)
        if not allowed:
            return None
        with self.connect() as conn:
            row = conn.execute(
                f"""
                SELECT *
                FROM memory_items
                WHERE id = ?
                  AND status = ?
                  AND privacy_class IN ({",".join("?" for _ in allowed)})
                LIMIT 1
                """,
                (memory_id, ACTIVE, *allowed),
            ).fetchone()
        return self._item_from_row(row) if row else None

    def _like_search(
        self,
        conn: sqlite3.Connection,
        query: str,
        allowed: tuple[str, ...],
        limit: int,
    ) -> list[sqlite3.Row]:
        like = f"%{query}%"
        return conn.execute(
            f"""
            SELECT *, 1.0 AS rank
            FROM memory_items
            WHERE status = ?
              AND privacy_class IN ({",".join("?" for _ in allowed)})
              AND (content LIKE ? OR kind LIKE ? OR tags_json LIKE ? OR source_ref LIKE ?)
            ORDER BY updated_at DESC
            LIMIT ?
            """,
            (ACTIVE, *allowed, like, like, like, like, limit),
        ).fetchall()

    def _retrieval_from_row(self, row: sqlite3.Row, query: str) -> Retrieval:
        item = self._item_from_row(row)
        token_overlap = set(tokenize(query)) & set(tokenize(" ".join((item.kind, item.content, " ".join(item.tags)))))
        score = max(0.0, 10.0 - float(row["rank"] if "rank" in row.keys() else 0.0))
        reason_bits = []
        if token_overlap:
            reason_bits.append("matched " + ", ".join(sorted(token_overlap)[:5]))
        if item.kind == "correction":
            reason_bits.append("correction memory governs drift prevention")
        if item.kind == "boundary":
            reason_bits.append("boundary memory blocks stale or unsafe state")
        if item.kind == "next_gate":
            reason_bits.append("next-gate memory preserves current workflow")
        reason = "; ".join(reason_bits) or "recent active memory"
        return Retrieval(item=item, reason=reason, score=score, token_estimate=max(1, len(item.content.split())))

    def _item_from_row(self, row: sqlite3.Row) -> MemoryItem:
        return MemoryItem(
            id=row["id"],
            kind=row["kind"],
            content=row["content"],
            source_ref=row["source_ref"],
            privacy_class=row["privacy_class"],
            confidence=float(row["confidence"]),
            status=row["status"],
            tags=tuple(json.loads(row["tags_json"] or "[]")),
            created_at=row["created_at"],
            updated_at=row["updated_at"],
            supersedes_id=row["supersedes_id"],
            expires_at=row["expires_at"],
        )

    def _log_retrievals(self, query: str, retrievals: list[Retrieval]) -> None:
        now = utc_now()
        with self.connect() as conn:
            for retrieval in retrievals:
                conn.execute(
                    """
                    INSERT INTO retrieval_log(query, memory_id, reason, score, token_estimate, created_at)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (
                        query,
                        retrieval.item.id,
                        retrieval.reason,
                        retrieval.score,
                        retrieval.token_estimate,
                        now,
                    ),
                )

    def list_items(self, status: str | None = None) -> list[MemoryItem]:
        with self.connect() as conn:
            if status:
                rows = conn.execute(
                    "SELECT * FROM memory_items WHERE status = ? ORDER BY updated_at DESC",
                    (status,),
                ).fetchall()
            else:
                rows = conn.execute("SELECT * FROM memory_items ORDER BY updated_at DESC").fetchall()
        return [self._item_from_row(row) for row in rows]

    def retrieval_events(self) -> list[dict[str, Any]]:
        with self.connect() as conn:
            rows = conn.execute(
                """
                SELECT query, memory_id, reason, score, token_estimate, created_at
                FROM retrieval_log
                ORDER BY id
                """
            ).fetchall()
        return [dict(row) for row in rows]

    def add_evidence_doc(
        self,
        *,
        id: str,
        title: str,
        body: str,
        source_ref: str,
        body_hash: str,
        privacy_class: str = "internal",
        metadata: dict[str, Any] | None = None,
        reason: str = "created",
    ) -> EvidenceDoc:
        now = utc_now()
        doc = EvidenceDoc(
            id=id,
            title=title.strip() or id,
            body=body.strip(),
            source_ref=source_ref.strip(),
            body_hash=body_hash,
            privacy_class=privacy_class,
            created_at=now,
            updated_at=now,
            metadata=metadata or {},
        )
        with self.connect() as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO evidence_docs
                    (id, title, body, source_ref, body_hash, privacy_class,
                     created_at, updated_at, metadata_json)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    doc.id,
                    doc.title,
                    doc.body,
                    doc.source_ref,
                    doc.body_hash,
                    doc.privacy_class,
                    doc.created_at,
                    doc.updated_at,
                    json.dumps(doc.metadata, sort_keys=True),
                ),
            )
            conn.execute("DELETE FROM evidence_fts WHERE id = ?", (doc.id,))
            conn.execute(
                "INSERT INTO evidence_fts(id, title, body, source_ref) VALUES (?, ?, ?, ?)",
                (doc.id, doc.title, doc.body, doc.source_ref),
            )
            conn.execute(
                """
                INSERT INTO evidence_events(evidence_id, event_type, reason, created_at, metadata_json)
                VALUES (?, ?, ?, ?, ?)
                """,
                (doc.id, "created", reason, now, json.dumps(doc.metadata, sort_keys=True)),
            )
        return doc

    def search_evidence(
        self,
        query: str,
        *,
        limit: int = 4,
        allowed_privacy: Iterable[str] = ("public", "internal"),
    ) -> list[EvidenceHit]:
        allowed = tuple(allowed_privacy)
        if not allowed:
            return []
        tokens = tokenize(query)
        rows: list[sqlite3.Row]
        with self.connect() as conn:
            if tokens:
                match = " OR ".join(tokens)
                try:
                    rows = conn.execute(
                        f"""
                        SELECT ed.*, bm25(evidence_fts) AS rank
                        FROM evidence_fts
                        JOIN evidence_docs ed ON ed.id = evidence_fts.id
                        WHERE evidence_fts MATCH ?
                          AND ed.privacy_class IN ({",".join("?" for _ in allowed)})
                        ORDER BY rank
                        LIMIT ?
                        """,
                        (match, *allowed, limit),
                    ).fetchall()
                except sqlite3.OperationalError:
                    rows = self._evidence_like_search(conn, query, allowed, limit)
            else:
                rows = conn.execute(
                    f"""
                    SELECT *, 0.0 AS rank
                    FROM evidence_docs
                    WHERE privacy_class IN ({",".join("?" for _ in allowed)})
                    ORDER BY updated_at DESC
                    LIMIT ?
                    """,
                    (*allowed, limit),
                ).fetchall()
        hits = [self._evidence_hit_from_row(row, query) for row in rows]
        self._log_evidence_retrievals(query, hits)
        return hits

    def _evidence_like_search(
        self,
        conn: sqlite3.Connection,
        query: str,
        allowed: tuple[str, ...],
        limit: int,
    ) -> list[sqlite3.Row]:
        like = f"%{query}%"
        return conn.execute(
            f"""
            SELECT *, 1.0 AS rank
            FROM evidence_docs
            WHERE privacy_class IN ({",".join("?" for _ in allowed)})
              AND (title LIKE ? OR body LIKE ? OR source_ref LIKE ?)
            ORDER BY updated_at DESC
            LIMIT ?
            """,
            (*allowed, like, like, like, limit),
        ).fetchall()

    def _evidence_hit_from_row(self, row: sqlite3.Row, query: str) -> EvidenceHit:
        doc = self._evidence_from_row(row)
        token_overlap = set(tokenize(query)) & set(tokenize(" ".join((doc.title, doc.body, doc.source_ref))))
        score = max(0.0, 10.0 - float(row["rank"] if "rank" in row.keys() else 0.0))
        reason = "matched " + ", ".join(sorted(token_overlap)[:5]) if token_overlap else "recent evidence document"
        return EvidenceHit(doc=doc, reason=reason, score=score, token_estimate=max(1, len(doc.body.split())))

    def _evidence_from_row(self, row: sqlite3.Row) -> EvidenceDoc:
        return EvidenceDoc(
            id=row["id"],
            title=row["title"],
            body=row["body"],
            source_ref=row["source_ref"],
            body_hash=row["body_hash"],
            privacy_class=row["privacy_class"],
            created_at=row["created_at"],
            updated_at=row["updated_at"],
            metadata=json.loads(row["metadata_json"] or "{}"),
        )

    def _log_evidence_retrievals(self, query: str, hits: list[EvidenceHit]) -> None:
        now = utc_now()
        with self.connect() as conn:
            for hit in hits:
                conn.execute(
                    """
                    INSERT INTO evidence_retrieval_log(query, evidence_id, reason, score, token_estimate, created_at)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (
                        query,
                        hit.doc.id,
                        hit.reason,
                        hit.score,
                        hit.token_estimate,
                        now,
                    ),
                )

    def list_evidence(self) -> list[EvidenceDoc]:
        with self.connect() as conn:
            rows = conn.execute("SELECT * FROM evidence_docs ORDER BY updated_at DESC").fetchall()
        return [self._evidence_from_row(row) for row in rows]

    def evidence_retrieval_events(self) -> list[dict[str, Any]]:
        with self.connect() as conn:
            rows = conn.execute(
                """
                SELECT query, evidence_id, reason, score, token_estimate, created_at
                FROM evidence_retrieval_log
                ORDER BY id
                """
            ).fetchall()
        return [dict(row) for row in rows]
