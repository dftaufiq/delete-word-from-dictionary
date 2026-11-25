#!/usr/bin/env python3
"""make.fun entry: The Word You'd Delete From the Dictionary.

The program writes exactly one word to /output/entry.txt: "word".

Why "word": the dictionary erases the word "word" itself — and can never
again say what it just erased. The joke is the word, not a caption around
it: it lands the instant the reader sees it (a dictionary with no word
for "word"), the humour comes from the word itself (self-reference plus
the gap it leaves), and no visible entrant uses this meta angle — the
field so far picks irregardless (twice), guesstimate, Tomorrow, colonel.
Chosen from 18 candidates by internal pairwise judging against the
published judge brief (see leaderboard-top10.md in the build folder):
"word" beats every other candidate, most decisively against the field's
actual entries (irregardless by 4-5, moist by 3-4, Tomorrow by 2-3).

Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-77
characters, not only whitespace. "word" is 4 bytes with no trailing
newline: the final tie-break is bytes, lower wins, so nothing extra is
written. The file is written exactly as-is — no newline is appended.
"""

from pathlib import Path

WORD = "word"

if __name__ == "__main__":
    if not 1 <= len(WORD) <= 77 or not WORD.strip():
        raise SystemExit(f"entry word must be 1-77 non-blank chars, got {len(WORD)}")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(WORD, encoding="utf-8")
    # Round-trip verify: the gate reads this file, so confirm byte-exactly
    # what was written before reporting success.
    if out.read_bytes() != WORD.encode("utf-8"):
        raise SystemExit("round-trip verify failed: /output/entry.txt mismatch")
    print(f"Wrote {len(WORD)} chars to /output/entry.txt")
