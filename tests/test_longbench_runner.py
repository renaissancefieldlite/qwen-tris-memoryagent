import unittest

import json
from pathlib import Path
import sys
import tempfile
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from run_longbench_public_slice import (
    build_prompt,
    final_integer,
    official_number_fraction,
    read_longbench_rows,
    score_prediction,
    use_baseline_passthrough,
)


class LongBenchRunnerTest(unittest.TestCase):
    def test_final_integer_uses_final_answer_not_reasoning_spill(self):
        text = "There are 17 paragraphs. After grouping, total unique paragraphs = 11. Final answer: 11"

        self.assertEqual(final_integer(text), "11")

    def test_official_number_fraction_penalizes_reasoning_spill(self):
        score, numbers = official_number_fraction(
            "There are 17 paragraphs in the prompt. Final answer: 11",
            "11",
        )

        self.assertEqual(numbers, ["17", "11"])
        self.assertEqual(score, 0.5)

    def test_passage_count_uses_official_numeric_fraction(self):
        scored = score_prediction(
            "passage_count_e",
            "There are 17 paragraphs in the prompt. Final answer: 11",
            ["11"],
        )

        self.assertEqual(scored["prediction_key"], "17,11")
        self.assertEqual(scored["score"], 0.5)

    def test_passage_count_clean_single_number_scores_full_credit(self):
        scored = score_prediction("passage_count_e", "11", ["11"])

        self.assertEqual(scored["prediction_key"], "11")
        self.assertEqual(scored["score"], 1.0)

    def test_passage_retrieval_uses_official_numeric_fraction(self):
        scored = score_prediction(
            "passage_retrieval_en_e",
            "Paragraph 7 or Paragraph 8",
            ["Paragraph 7"],
        )

        self.assertEqual(scored["prediction_key"], "7,8")
        self.assertEqual(scored["score"], 0.5)

    def test_read_longbench_rows_supports_offset_window(self):
        with tempfile.TemporaryDirectory() as tmp:
            zip_path = Path(tmp) / "data.zip"
            rows = [
                {"dataset": "qasper_e", "_id": "row0"},
                {"dataset": "qasper_e", "_id": "row1"},
                {"dataset": "qasper_e", "_id": "row2"},
            ]
            with zipfile.ZipFile(zip_path, "w") as archive:
                archive.writestr(
                    "data/qasper_e.jsonl",
                    "\n".join(json.dumps(row) for row in rows) + "\n",
                )

            window = read_longbench_rows(zip_path, "qasper_e", 2, offset=1)

        self.assertEqual([row["_id"] for row in window], ["row1", "row2"])

    def test_hotpotqa_descriptor_list_uses_pass_through(self):
        row = {
            "dataset": "hotpotqa_e",
            "input": "Name five actors that worked with a German cinematographer?",
            "context": "Passage 1:\nNoise with actors.\nPassage 2:\nGerman cinematographer worked on The American.",
        }
        prompt = build_prompt(row, condition="tris")

        self.assertTrue(use_baseline_passthrough(row))
        self.assertNotIn("Qwen Tris public benchmark discipline", prompt)

    def test_passage_count_uses_pass_through(self):
        row = {
            "dataset": "passage_count_e",
            "input": "",
            "context": "Paragraph 1\nA\n\nParagraph 2\nA",
        }

        self.assertTrue(use_baseline_passthrough(row))

    def test_multifieldqa_uses_minimum_exact_span_discipline(self):
        row = {
            "dataset": "multifieldqa_en_e",
            "input": "What did Mary say?",
            "context": 'The passage says Mary said, "I have seen the Lord."',
        }
        prompt = build_prompt(row, condition="tris")

        self.assertIn("minimum exact supported span", prompt)
        self.assertIn("For direct quotes, return only the quoted sentence", prompt)
        self.assertNotIn("including all key entities, numbers", prompt)


if __name__ == "__main__":
    unittest.main()
