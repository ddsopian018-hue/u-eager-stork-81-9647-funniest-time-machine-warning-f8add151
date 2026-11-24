"""Funniest Time Machine Warning Label.

Writes a single one-line warning label for a time machine to
$MAKEFUN_OUTPUT_DIR/entry.txt (or ./output/entry.txt as a fallback).

Pure standard library, no network, no secrets, no hard-coded paths.
"""

import os
import sys

# The label: a straight-face safety notice. The hazard is the
# grandfather paradox; the twist lands in the last few words.
LABEL = (
    "WARNING: Never use this machine to prevent your own birth. "
    "Unborn passengers will be billed for the trip anyway."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        # No trailing newline: the file is exactly the label, 112 chars.
        f.write(LABEL)
    return 0


if __name__ == "__main__":
    sys.exit(main())
