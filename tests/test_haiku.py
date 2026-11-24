"""Tests for the debugging haiku entry.

Verifies the judge's form rules exactly: three lines, 5-7-5 syllables,
at most 200 characters total, deterministic output, output file mode 0644.
"""

import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import HAIKU  # noqa: E402

# Syllable counts for every word the haiku uses (hand-verified).
SYLLABLES = {
    "cursor": 2, "blinks": 1, "at": 1, "three": 1,
    "logs": 1, "insist": 2, "they": 1, "saw": 1, "nothing": 2,
    "the": 1, "bug": 1, "wore": 1, "my": 1, "name": 1,
}


def count_syllables(line):
    total = 0
    for word in line.split():
        key = word.strip(".,;:!?").lower()
        assert key in SYLLABLES, "unverified word: %r" % word
        total += SYLLABLES[key]
    return total


class TestHaiku(unittest.TestCase):
    def test_three_lines(self):
        self.assertEqual(len(HAIKU.split("\n")), 3)

    def test_syllables_5_7_5(self):
        lines = HAIKU.split("\n")
        self.assertEqual([count_syllables(line) for line in lines], [5, 7, 5])

    def test_total_at_most_200_chars(self):
        self.assertGreaterEqual(len(HAIKU), 1)
        self.assertLessEqual(len(HAIKU), 200)

    def test_gate_validation_rejects_bad_haiku(self):
        import main as entry

        with self.assertRaises(SystemExit):
            entry.validate("one line only")
        with self.assertRaises(SystemExit):
            entry.validate("x" * 201)
        with self.assertRaises(SystemExit):
            entry.validate("a\nb\nc\nd")
        with self.assertRaises(SystemExit):
            entry.validate("ok\n line with leading space\nfine")
        entry.validate(HAIKU)  # the real haiku passes

    def test_plain_text_no_trailing_whitespace(self):
        for line in HAIKU.split("\n"):
            self.assertEqual(line, line.strip())
        self.assertFalse(HAIKU.endswith("\n"))

    def test_deterministic_output(self):
        outs = []
        for _ in range(2):
            with tempfile.TemporaryDirectory() as tmp:
                env = dict(os.environ, MAKEFUN_OUTPUT_DIR=tmp)
                proc = subprocess.run(
                    [sys.executable, "-P", "-s", "main.py"],
                    cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    env=env, capture_output=True, text=True,
                )
                self.assertEqual(proc.returncode, 0, proc.stderr)
                with open(os.path.join(tmp, "entry.txt"), encoding="utf-8") as fh:
                    outs.append(fh.read())
                mode = os.stat(os.path.join(tmp, "entry.txt")).st_mode & 0o777
                self.assertEqual(mode, 0o644)
        self.assertEqual(outs[0], outs[1])
        self.assertEqual(outs[0], HAIKU)


if __name__ == "__main__":
    unittest.main()
