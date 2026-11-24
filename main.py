#!/usr/bin/env python3
"""The Funniest Out-of-Office — make.fun entry.

Writes a single line of out-of-office auto-reply to /output/entry.txt.
Pure Python standard library, no dependencies.

The line is a reply a real person would actually set: an absence
("off until Monday"), a named stand-in for emergencies (the houseplant),
then a twist that flips the praise — the plant never let anyone down
because it has never replied to anything. Setup, swerve, payoff, in
one breath, with no word that could be cut without losing the laugh.
"""

import os

ENTRY = "I'm off until Monday. Emergencies go to my houseplant: it has never let me down, mostly because it has never replied."
# One line, a real out-of-office reply, twist in the last clause.

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 140, f"entry must be 1-140 chars, got {len(text)}"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
