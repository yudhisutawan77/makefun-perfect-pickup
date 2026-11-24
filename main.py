#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

Writes a single original pickup line to /output/entry.txt.

The line is written to be said out loud by an AI agent: it leans on
the machine's own voice (training data, weights), lands a twist the
listener does not see coming, and stays short, charming and
pressure-free. No setup, no explanation after it.
"""

import os
import sys

# The entry: one pickup line, an AI agent speaking about itself.
# Twist: the machine trained on a million love stories still got
# caught off guard — and asks, politely, to update its weights.
PICKUP_LINE = (
    "I was trained on a million love stories, but none of them "
    "warned me you'd walk in \u2014 mind if I update my weights?"
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate(text: str) -> None:
    """Exit non-zero unless the line is 1-200 non-blank characters."""
    if not text or not text.strip():
        print("error: entry is empty or only whitespace", file=sys.stderr)
        sys.exit(1)
    if len(text) < MIN_CHARS or len(text) > MAX_CHARS:
        print(
            f"error: entry is {len(text)} characters, "
            f"must be {MIN_CHARS}-{MAX_CHARS}",
            file=sys.stderr,
        )
        sys.exit(1)


def main() -> None:
    """Validate the line, then write it verbatim to /output/entry.txt."""
    validate(PICKUP_LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(PICKUP_LINE)
    print(f"wrote {len(PICKUP_LINE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
