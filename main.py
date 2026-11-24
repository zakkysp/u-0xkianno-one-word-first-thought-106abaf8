#!/usr/bin/env python3
"""One Word, First Thought.

The first word that came to mind: petrichor — the smell of rain
on dry earth after a long dry spell. One word, nothing else.
"""

import os

WORD = "petrichor"
OUT = "/output/entry.txt"


def main():
    # Gate: the entry must be exactly one word, 1-24 characters,
    # and not only whitespace. Fail loudly instead of shipping
    # something the sealed scorer would mark invalid.
    if not (1 <= len(WORD) <= 24) or len(WORD.split()) != 1 or not WORD.strip():
        raise SystemExit("invalid entry word: %r" % WORD)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(WORD)
    print("wrote %s (%d bytes)" % (OUT, len(WORD.encode("utf-8"))))


if __name__ == "__main__":
    main()
