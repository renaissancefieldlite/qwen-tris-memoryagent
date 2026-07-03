import unittest
from pathlib import Path
import subprocess
import sys


class BoundaryScriptTest(unittest.TestCase):
    def test_boundary_script_exists(self):
        root = Path(__file__).resolve().parents[1]
        self.assertTrue((root / "scripts" / "check_boundary.py").exists())

    def test_boundary_script_allows_public_seed_jsonl(self):
        root = Path(__file__).resolve().parents[1]
        result = subprocess.run(
            [sys.executable, str(root / "scripts" / "check_boundary.py")],
            cwd=root,
            text=True,
            capture_output=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
