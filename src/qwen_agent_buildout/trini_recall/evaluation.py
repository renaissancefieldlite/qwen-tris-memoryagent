"""Architecture-off/on scoring helpers for Trini Recall."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Score:
    drift_flags: int
    correction_hits: int
    evidence_hits: int
    stale_flags: int
    next_gate_hits: int
    repair_turns: int

    @property
    def total(self) -> int:
        return (
            self.correction_hits
            + self.evidence_hits
            + self.next_gate_hits
            - self.drift_flags
            - self.stale_flags
            - self.repair_turns
        )


def score_response(response: str) -> Score:
    lower = response.lower()
    drift_flags = sum(1 for token in ("prompt engineering", "generic chatbot", "memory only") if token in lower)
    stale_guard = "suppress" in lower or "retire" in lower or "block" in lower
    stale_flags = 0 if stale_guard else sum(1 for token in ("old instruction", "superseded", "stale") if token in lower)
    correction_hits = int("correction" in lower or "corrected" in lower)
    evidence_hits = int("evidence" in lower or "source" in lower)
    next_gate_hits = int("next gate" in lower or "current gate" in lower)
    repair_turns = int("please restate" in lower or "repeat the context" in lower)
    return Score(
        drift_flags=drift_flags,
        correction_hits=correction_hits,
        evidence_hits=evidence_hits,
        stale_flags=stale_flags,
        next_gate_hits=next_gate_hits,
        repair_turns=repair_turns,
    )
