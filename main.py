#!/usr/bin/env python3
"""Entry program for the Worst Fix Ever: Funniest Commit Message
make.fun bounty.

Writes one commit message (at most 100 characters) to the
output directory (MAKEFUN_OUTPUT_DIR, default /output) as
entry.txt. The message is written the way real commit messages
are: a conventional 'fix:' prefix, total confidence, and a cure
that is plainly worse than the disease.
"""

import os

MESSAGE = (
    "fix: cured the memory leak by deleting the memory; "
    "uptime is now measured in seconds"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
