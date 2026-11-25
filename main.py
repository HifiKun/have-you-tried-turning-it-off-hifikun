#!/usr/bin/env python3
"""Have You Tried Turning It Off? - make.fun entry.

Writes one funny line from a hopeless tech support agent to a
desperate customer into /output/entry.txt (or ./output/entry.txt
when run locally).
"""

import os

LINE = (
    "Have you tried turning it off and on again? Perfect, that was step one. "
    "Steps two through twelve are the same step, done slower, with feeling."
)


def main() -> None:
    line = LINE.strip()
    assert line, "entry must not be empty"
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 199, f"entry must be 1-199 chars, got {len(line)}"
    out_dir = "/output" if os.path.isdir("/output") else "output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
