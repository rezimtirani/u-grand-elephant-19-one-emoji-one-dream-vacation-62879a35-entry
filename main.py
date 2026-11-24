#!/usr/bin/env python3
"""One Emoji, One Dream Vacation - make.fun entry.

Writes exactly one emoji to $MAKEFUN_OUTPUT_DIR/entry.txt:
Mount Fuji (U+1F5FB), a single postcard of a dream trip.
"""

import os
import sys


DREAM_EMOJI = "\U0001F5FB"


def entry_text():
    """Return the single emoji that stands in for the dream vacation."""
    return DREAM_EMOJI


def validate_entry(text):
    """Check the entry against the sealed gate: 1-8 UTF-8 chars, not blank."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry must not be only white space")
    if not 1 <= len(stripped) <= 8:
        raise ValueError("entry must be 1 to 8 characters")
    if stripped != text:
        raise ValueError("entry must be exactly one emoji, nothing else")
    return stripped


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(validate_entry(entry_text()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
