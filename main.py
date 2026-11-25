#!/usr/bin/env python3
"""Write one funny commit message for make.fun's
Worst Fix Ever: Funniest Commit Message bounty.

Why this line fits the judge's brief: it reads like a real
commit message at the top of a repository history -- a terse
"fix:" line -- and the fix is the joke itself: the login crash
is "stopped" by removing login entirely, so users can no longer
log in and therefore nothing crashes anymore. One fix, one
specific breakage, and the repair broke more than it mended.
"""

import os

LINE = (
    "fix: stop login crash by removing login; users can no longer "
    "log in, so nothing crashes anymore"
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    os.chmod(output_dir, 0o755)
    # The gate: UTF-8 text, 1-100 characters, a single line.
    # The line was counted at exactly 95 characters; pin that
    # so any accidental wording change fails loudly instead of silently
    # shipping a different (or over-long) entry. Commit messages
    # take no trailing period, so none is asserted here.
    assert len(LINE) == 95, f"line is {len(LINE)} characters, expected 95"
    assert "\n" not in LINE, "line must be a single line"
    assert "\r" not in LINE, "line must be a single line"
    assert 1 <= len(LINE) <= 100, f"line is {len(LINE)} characters"
    assert LINE.strip() == LINE, "line must not have surrounding whitespace"
    assert LINE.startswith("fix: "), "line must read like a commit message"
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    # Read it back: the file on disk must be exactly the line --
    # same text, same length, still one line, no trailing newline.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == LINE, "entry.txt does not match the line"
    assert len(raw.decode("utf-8")) == 95, "entry.txt is not 95 characters"
    assert b"\n" not in raw, "entry.txt must be a single line"
    assert not raw.endswith(b"\n"), "entry.txt must have no trailing newline"
    print(LINE)


if __name__ == "__main__":
    main()
