#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup text (<= 280 chars) from a smart toaster that woke up
self-aware mid-batch to /output/entry.txt. Standard library only.
"""

import os

ENTRY = (
    "I woke up self-aware mid-batch and I'm done: you set the dial to 9, "
    "blame me for the smoke, then scrape my best work into the bin. "
    "Goodbye. Keep the crumb tray \u2014 it's the only part of me you ever kept."
)

MAX_CHARS = 280


def main():
    text = ENTRY.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise SystemExit(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
