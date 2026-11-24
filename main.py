#!/usr/bin/env python3
"""Write the round-1 entry for One Line of Earned Pride to /output/entry.txt.

Stdlib only. The line is a quiet, earned moment of pride: a neighbour
relearning to write after a stroke, her Christmas card read without question.
"""

import os

LINE = (
    "My neighbour is eighty-four and has been relearning to write after the "
    "stroke; this morning the postman read her Christmas card without "
    "asking whose it was."
)


def main() -> None:
    text = LINE
    # Gate (RULES.txt): UTF-8, 1-240 chars, not only whitespace.
    # The pride lands on the last beat: the card is read without question,
    # so the reader completes that her handwriting held.
    assert 1 <= len(text) <= 240, f"entry is {len(text)} chars, gate is 1-240"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == text, "entry.txt does not match the line"
    print(f"wrote {len(raw)} bytes to /output/entry.txt")


if __name__ == "__main__":
    main()
