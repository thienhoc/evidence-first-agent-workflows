import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ValidatorTests(unittest.TestCase):
    def test_public_examples_pass(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "tools" / "validate_records.py"), str(ROOT / "examples")],
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("PASS: 3 records validated", result.stdout)


if __name__ == "__main__":
    unittest.main()
