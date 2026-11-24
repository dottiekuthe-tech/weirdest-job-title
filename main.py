"""Weirdest Job Title: Blind Judge Showdown.

Writes one job title (37 characters) to /output/entry.txt:
the weirdest job title, a few words and nothing else.
Pure Python 3.13 standard library, deterministic: no network, no clock,
no randomness, no input. Two runs write byte-identical output.
"""

import os
import sys

# Chosen title: a real job frame (pet psychic) plus one hilariously
# specific twist — a goldfish, famous for a three-second memory, with
# anxiety. Sounds like a real job, specific enough to picture the person
# doing it, twist lands on the first read. 37 characters, inside the
# 1-60 gate. Avoids the field's saturated Senior/Chief/VP-of-X frame
# and the Apologizer angle.
# Revision note: wording unchanged since v1; the title was picked over
# six other candidates (see candidates.md) for its specific twist.
TITLE = "Pet Psychic for Goldfish With Anxiety"


# Bounty gate: the entry must be one job title of 1-60 UTF-8 characters.
MAX_CHARS = 60


def main() -> None:
    if len(TITLE) > MAX_CHARS:
        print(f"entry too long: {len(TITLE)} chars (max {MAX_CHARS})", file=sys.stderr)
        sys.exit(1)
    # Output goes to $MAKEFUN_OUTPUT_DIR/entry.txt in the harness,
    # or /output/entry.txt when run locally by hand.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TITLE)


if __name__ == "__main__":
    main()
