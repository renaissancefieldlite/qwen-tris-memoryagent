from pathlib import Path
import json
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from qwen_agent_buildout.trini_recall import MemoryStore, OfflineProvider, TriniRecallAgent


class TriniRecallMemoryTest(unittest.TestCase):
    def test_retrieves_correction_with_reason(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = MemoryStore(Path(tmp) / "memory.sqlite3")
            store.add_memory(
                id="correction_1",
                kind="correction",
                content="Stable-state architecture is the lynchpin for memory recall.",
                source_ref="docs/test.md",
                tags=("stable-state", "memory"),
                privacy_class="public",
            )

            retrievals = store.retrieve("How does stable state help memory recall?")

        self.assertEqual(retrievals[0].item.id, "correction_1")
        self.assertIn("correction memory", retrievals[0].reason)

    def test_architecture_on_uses_memory_and_baseline_does_not(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            store = MemoryStore(root / "data" / "memory.sqlite3")
            store.add_memory(
                id="next_gate",
                kind="next_gate",
                content="Pipe Qwen Cloud API after the credit lands.",
                source_ref="track_packets/track1_memoryagent.md",
                tags=("qwen", "api"),
                privacy_class="internal",
            )
            agent = TriniRecallAgent(
                store=store,
                provider=OfflineProvider(),
                task_state="Track 1 scaffold",
                current_gate="Qwen API gate",
            )

            baseline = agent.answer("What is the Qwen API gate?", architecture_on=False)
            architecture_on = agent.answer("What is the Qwen API gate?", architecture_on=True)

        self.assertEqual(len(baseline.retrievals), 0)
        self.assertGreaterEqual(len(architecture_on.retrievals), 1)
        self.assertIn("TRINI RECALL STABLE-STATE PACKET", architecture_on.prompt)

    def test_evidence_docs_are_rag_retrieved_and_prompted(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = MemoryStore(Path(tmp) / "memory.sqlite3")
            store.add_evidence_doc(
                id="doc_1",
                title="Qwen Agent Memory",
                body="Qwen-Agent supports planning, tool usage, memory, RAG, and MCP workflows.",
                source_ref="docs/qwen-agent.md",
                body_hash="abc123",
                privacy_class="public",
            )
            agent = TriniRecallAgent(
                store=store,
                provider=OfflineProvider(),
                task_state="Track 1 scaffold",
                current_gate="Qwen API gate",
            )

            result = agent.answer("How should Trini use Qwen-Agent memory and RAG?", architecture_on=True)

        self.assertEqual(result.evidence_hits[0].doc.id, "doc_1")
        self.assertIn("Retrieved evidence/RAG", result.prompt)

    def test_memory_stress_seed_files_are_source_backed(self):
        dataset_dir = ROOT / "datasets" / "memory_stress"
        seed_files = sorted(dataset_dir.glob("*_seed.jsonl"))

        self.assertGreaterEqual(len(seed_files), 5)

        task_ids = set()
        families = set()
        for seed_file in seed_files:
            with seed_file.open("r", encoding="utf-8") as handle:
                rows = [json.loads(line) for line in handle if line.strip()]

            self.assertGreaterEqual(len(rows), 1, seed_file.name)
            for row in rows:
                task_ids.add(row["task_id"])
                families.add(row["family"])
                self.assertTrue(row["source_ref"])
                self.assertTrue(row["active_memory"])
                self.assertTrue(row["query"])
                self.assertTrue(row["expected_recall"])
                self.assertTrue(row["success_gate"])

        self.assertIn("c5b_500_ssp_memory", families)
        self.assertEqual(len(task_ids), sum(1 for seed_file in seed_files for line in seed_file.read_text(encoding="utf-8").splitlines() if line.strip()))


if __name__ == "__main__":
    unittest.main()
