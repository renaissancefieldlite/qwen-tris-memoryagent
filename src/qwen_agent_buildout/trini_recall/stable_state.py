"""Stable-state packet builder for Trini Recall."""

from __future__ import annotations

from dataclasses import dataclass, field

from .memory_store import Retrieval


@dataclass(frozen=True)
class StableStatePacket:
    """The currentness layer that makes memory useful."""

    task_state: str
    current_gate: str
    constraints: tuple[str, ...] = field(default_factory=tuple)
    corrections: tuple[str, ...] = field(default_factory=tuple)
    evidence_boundaries: tuple[str, ...] = field(default_factory=tuple)
    recalled_memories: tuple[Retrieval, ...] = field(default_factory=tuple)

    def render(self, token_budget: int = 1200) -> str:
        lines = [
            "TRINI RECALL STABLE-STATE PACKET",
            f"Task state: {self.task_state}",
            f"Current gate: {self.current_gate}",
            "",
            "Constraints:",
        ]
        lines.extend(f"- {item}" for item in self.constraints or ("none",))
        lines.append("")
        lines.append("Corrections:")
        lines.extend(f"- {item}" for item in self.corrections or ("none",))
        lines.append("")
        lines.append("Evidence boundaries:")
        lines.extend(f"- {item}" for item in self.evidence_boundaries or ("none",))
        lines.append("")
        lines.append("Retrieved memories with reasons:")
        if self.recalled_memories:
            for retrieval in self.recalled_memories:
                lines.append(
                    f"- [{retrieval.item.id}] {retrieval.item.kind}: "
                    f"{retrieval.item.content} "
                    f"(source={retrieval.item.source_ref}; reason={retrieval.reason})"
                )
        else:
            lines.append("- none")

        rendered = "\n".join(lines)
        words = rendered.split()
        if len(words) <= token_budget:
            return rendered
        return " ".join(words[:token_budget]) + "\n[stable-state packet truncated to budget]"

