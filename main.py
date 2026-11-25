#!/usr/bin/env python3
"""Office Joke Open entry.

Writes one single-line office joke to /output/entry.txt.
The joke: the office printer only ever jams on the one page you
actually need -- because it has read your performance review.

Deterministic, no network, no arguments: run `python3 main.py`.
"""

import os

JOKE = (
    "The office printer only jams on the page I actually need, "
    "which is how I know it has read my performance review."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"Wrote {len(JOKE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
