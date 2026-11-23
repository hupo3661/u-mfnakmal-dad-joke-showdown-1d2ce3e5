#!/usr/bin/env python3
"""Write one original dad joke to /output/entry.txt.

The joke is a barbecue dad joke: a clean steaks/stakes pun, told
straight-faced, punchline at the end, short enough to land on the
first read and to be delivered across a dinner table.
Standard library only, no network, no input files.
"""

import os

JOKE = "I brought a ladder to the barbecue. I heard the steaks were high."


def main() -> None:
    if "\n" in JOKE or "\r" in JOKE:
        raise SystemExit("Joke payload must be a single line (no newline characters).")
    if not JOKE.strip():
        raise SystemExit("Joke payload must be non-empty.")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
