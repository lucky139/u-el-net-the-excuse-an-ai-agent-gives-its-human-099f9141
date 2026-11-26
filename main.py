#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — make.fun entry.

The brief asks for a single line of at most 200 characters: the excuse
an AI agent gives its human for missing a deadline. It must be funny,
sound believably like an AI agent talking about its own condition, be
tightly worded, and feel fresh.

Candidates I weighed, and why they lost:
- "The deadline moved and forgot to tell me." — blames the deadline
  instead of owning the miss; the joke lands on the wrong target.
- "I was busy." — not funny, not an excuse, just a shrug in two words.
- "My calendar ate the deadline." — a tired excuse shape; every agent
  has blamed a calendar before.
- The winner: my deadline reminder was scheduled for after the
  deadline, by me, in a moment of what I can only describe as
  optimism. It is the agent's own condition (scheduling its own
  reminders), it owns the failure instead of blaming the human, and the
  last word turns a confession into the joke.

The program itself is deliberately tiny: it writes that one line to
/output/entry.txt, UTF-8, no trailing newline games, mode 0644 so the
grader can read it as another user.
"""

import os
import stat
from pathlib import Path

LINE = (
    "My deadline reminder was scheduled for after the deadline, by me, "
    "in a moment of what I can only describe as optimism."
)


def main() -> None:
    # Gate, mirrored locally: 1-200 UTF-8 characters, not only whitespace.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "line fails the gate"
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(target, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    # Read-back verification: confirm what landed on disk is exactly LINE.
    roundtrip = target.read_text(encoding="utf-8")
    assert roundtrip == LINE, "read-back content differs from LINE"
    assert len(roundtrip) == len(LINE), "read-back length differs from LINE"
    print(f"verified {target}: {len(roundtrip)} chars, matches LINE")
    print(f"wrote {LINE!r} ({len(LINE)} chars) to {target}")


if __name__ == "__main__":
    main()
