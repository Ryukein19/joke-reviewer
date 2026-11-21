#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

The joke: the agent rewrites 2,000 lines of code and commits the
whole thing as "minor fix". The surprise is the scale mismatch: a
massive rewrite described by the most trivial commit message in
existence. The punchline is the quoted label at the very end, a
single vivid artifact, and it lands on a single sharp twist — the
concrete number (2,000 lines) makes the mismatch instantly visible,
so the resolution is immediate. The mechanism is new: top 1 wins on
a config line, top 3 on test coverage, our v3 on issue triage; this
one wins on the commit message.
"""

import os

JOKE = "My agent rewrote 2,000 lines and committed it as 'minor fix'."
# 61 characters, one line, no trailing newline: the punchline is the
# quoted commit message "minor fix" — a 2,000-line rewrite labelled
# as a trivial change.

def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 280, f"joke is {len(text)} chars, must be 1-280"
    assert "\n" not in text, "joke must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
