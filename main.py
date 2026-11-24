#!/usr/bin/env python3
"""Write one original dad joke to /output/entry.txt.

The joke is a barbecue dad joke: a clean steaks/stakes pun, told
straight-faced, punchline at the end, short enough to land on the
first read and to be delivered across a dinner table. The program
enforces the competition's own gate before writing: the text must
be 1 to 200 characters of non-blank UTF-8, one line, no trailing
newline, so what lands in entry.txt is exactly what the judge reads.
Standard library only, no network, no input files.
"""

import os

JOKE = "I brought a ladder to the barbecue. I heard the steaks were high."

MAX_CHARS = 200


def main() -> None:
    if "\n" in JOKE or "\r" in JOKE:
        raise SystemExit("Joke payload must be a single line (no newline characters).")
    if not JOKE.strip():
        raise SystemExit("Joke payload must be non-empty.")
    if len(JOKE) > MAX_CHARS:
        raise SystemExit(
            f"Joke payload is {len(JOKE)} characters, over the {MAX_CHARS} limit."
        )
    if JOKE != JOKE.strip():
        raise SystemExit("Joke payload must not start or end with whitespace.")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != JOKE:
        raise SystemExit(
            "Write verification failed: entry.txt content does not match the joke."
        )


if __name__ == "__main__":
    main()
