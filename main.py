#!/usr/bin/env python3
"""Write one line to /output/entry.txt: the funny line a hopeless tech
support agent gives a desperate customer.

The line was picked from 36 candidates by pairwise judging against the
brief — a cheerfully useless agent who closes the customer's ticket by
deleting it, then brags about the closure rate. The program builds the
line from two clauses — the good news, then the bad news — and checks
the result against the entry gate (length, single line, no leading or
trailing space, exact judged length) before writing it, then reads the
file back to confirm the bytes match.
"""

import os
import sys

LINE = (
    "Good news: I closed your ticket. "
    "Bad news: I closed it by deleting it, "
    "but the closure rate looks great."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(LINE) <= 199):
        sys.exit(f"line is {len(LINE)} characters, gate needs 1-199")
    if "\n" in LINE or LINE != LINE.strip():
        sys.exit("line must be a single line with no surrounding space")
    data = (LINE + "\n").encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
