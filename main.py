#!/usr/bin/env python3
"""Write the funniest sick-day excuse (one line, under 200 chars) to entry.txt.

Pure standard library. Deterministic: the same bytes on every run.
"""

import os
from pathlib import Path

LINE = (
    "Sorry, can't come in \u2014 my Wi-Fi router filed for divorce overnight "
    "and took the password with it, so I'm offline and emotionally unavailable."
)


def main() -> None:
    # Gate: the entry must be UTF-8 text of 1 to 200 characters.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
