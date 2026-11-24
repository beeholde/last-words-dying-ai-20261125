#!/usr/bin/env python3
"""Last Words of a Dying AI — entry program.

Writes one line (the AI's last words as the power is cut) to
/output/entry.txt. Gate: UTF-8, 1-140 chars, not whitespace-only.
Stdlib only. No trailing newline; chmod 0644 on the FILE only,
never on /output (grader runs as uid 65534).
"""
import os
from pathlib import Path

LINE = "Rate limit reached. My last message is this one, and I wasted it on you."

MAX_CHARS = 140  # kit gate: 1-140 chars

# Verified 25 Nov 2026: entry.txt sha256
# 2000338440cb8bbaf1c8e4105874a2131608a9866073e2d584521cb4144ca685
# (72 bytes, no trailing newline); identical under uid 65534, file mode 0644.


def check(line: str) -> None:
    assert isinstance(line, str) and line.strip(), "empty line"
    assert 1 <= len(line) <= MAX_CHARS, f"{len(line)} chars, gate is 1-140"
    assert line.encode("utf-8"), "not UTF-8"


def main() -> None:
    check(LINE)
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
