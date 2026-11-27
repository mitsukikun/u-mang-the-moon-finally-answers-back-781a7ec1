#!/usr/bin/env python3
"""The Moon Finally Answers Back -- make.fun entry #210.

A single line in the voice of the Moon, answering at last after four
billion years of wishes, howls and late-night promises. No network access;
writes only to /output/entry.txt and a copy beside this script.
"""

import os

ENTRY = (
    "Four billion years of wishes, howls, and 3 a.m. promises — and not "
    "one of you ever asked how I'm doing. I'm tired, I'm cratered, and "
    "the cheese stays mine."
)


def main() -> None:
    line = ENTRY.strip()
    # Gate: UTF-8, 1-240 characters, not only whitespace, a single line.
    assert line, "entry must not be blank"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 240, f"entry length {len(line)} outside 1-240"
    line.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)
    here = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    with open(here, "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
