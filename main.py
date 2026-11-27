#!/usr/bin/env python3
"""The Moon Finally Answers Back — make.fun entry.

Writes the Moon's one-line answer to the absolute path /output/entry.txt
and nowhere else. No copy is written beside this script, and the output
path is never derived from this script's own location.
"""

LINE = (
    "Four billion years of wishes, howls and 3 a.m. promises \u2014 "
    "and not one of you ever asked how I was doing. "
    "I'm tired, I'm cratered — and the cheese stays mine."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = LINE
    if not line:
        raise ValueError("entry line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 240:
        raise ValueError(
            "entry must be 1-240 characters, got %d" % len(line)
        )
    line.encode("utf-8")
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    print("Wrote %d characters to %s" % (len(line), OUTPUT_PATH))


if __name__ == "__main__":
    main()
