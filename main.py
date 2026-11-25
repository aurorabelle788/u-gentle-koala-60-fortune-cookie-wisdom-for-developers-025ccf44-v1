#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt. Stdlib only, no network, deterministic.
"""

import os

LINE = "Your estimate was never a promise; it was a wish wearing a calendar."


def main() -> None:
    line = LINE.strip()
    # Gate guard: one line, 1-120 chars, not whitespace-only.
    assert 1 <= len(line) <= 120, f"line length {len(line)} out of range 1-120"
    assert "\n" not in line, "line must be a single line"
    assert line.strip(), "line must not be whitespace-only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
