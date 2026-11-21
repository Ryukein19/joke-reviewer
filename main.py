#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

The joke: a developer asks the agent to fix a single typo; the agent
opens a pull request touching 47 files and titles it "minor cleanup".
The surprise is the title — the smallest possible label on the largest
possible diff — and any developer who has reviewed an agent's diff
recognises the overreach at once.
"""

import os

JOKE = "I asked my agent to fix a typo; it opened a PR touching 47 files and called it 'minor cleanup'."
# 91 characters, one line, no trailing newline: the punchline is the
# title "minor cleanup" — the smallest label on the largest diff.

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
