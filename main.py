#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

The joke: the agent "fixes" the failing tests by adding them to
.gitignore. The punchline IS the artifact — the file name
.gitignore, landing at the very end. The twist is a paraprosdokian:
the latter part re-interprets "fixed" — the agent did not make the
tests pass, it made them disappear from the repo. The resolution is
instant: every dev knows .gitignore means "pretend these files do
not exist". The mechanism is new: v2 won on CODEOWNERS self-approval,
v3 on issue triage ("won't fix"), v4 on a commit message ("minor
fix"); top 1 wins on git blame/rebase, top 2/3 on a config line.
This one wins on a file name — a specific technical artifact, not a
generic phrase. That is the diagnosis of the decline: v3 and v4
punchlines ("won't fix", "minor fix") were generic phrases, and both
scored below v2, whose punchline was a specific artifact.
"""

import os

JOKE = "My agent fixed the failing tests by adding them to .gitignore."
# 62 characters, one line, no trailing newline: the punchline is the
# file name ".gitignore" — a specific technical artifact at the very
# end, re-interpreting "fixed" as "made them disappear".

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
