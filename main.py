#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — make.fun entry.

Writes one haiku about debugging (5-7-5 syllables, three lines, plain
text) to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).

Pure standard library, fully deterministic: the same bytes on every run.
"""

import os
import sys

HAIKU = (
    "Cursor blinks at three\n"
    "logs insist they saw nothing\n"
    "the bug wore my name"
)


def validate(haiku):
    """Fail loudly if the haiku breaks the bounty gate.

    Gate: UTF-8 text, 1-200 characters, exactly three lines, no
    leading/trailing whitespace on any line. A bad haiku must never
    be written out — fail here instead of shipping an invalid entry.
    """
    if not 1 <= len(haiku) <= 200:
        raise SystemExit(
            "haiku is %d characters, outside the 1-200 gate" % len(haiku)
        )
    lines = haiku.split("\n")
    if len(lines) != 3:
        raise SystemExit("haiku has %d lines, expected exactly 3" % len(lines))
    for line in lines:
        if line != line.strip():
            raise SystemExit(
                "haiku line has leading/trailing whitespace: %r" % line
            )


def main() -> int:
    validate(HAIKU)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(HAIKU)
    os.chmod(path, 0o644)
    print("wrote %s (%d characters)" % (path, len(HAIKU)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
