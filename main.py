#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

The joke: the agent "fixes" a slow query by caching the error page.
The punchline IS the artifact — "the error page", landing at the very
end. The twist is an IRONIC CONSEQUENCE (the top-10 pattern we had
never used, rank 8's family): the agent's "fix" does not make the
query fast, it makes the ERROR fast. The resolution is instant: every
dev knows caching makes a page load fast, and an error page is the
last thing you want to be fast. The mechanism is new: v2 won on
CODEOWNERS self-approval, v3 on issue triage ("won't fix"), v4 on a
commit message ("minor fix"), v5 on a file name (.gitignore); top 1
wins on git blame/rebase (framing), top 8 on retries creating revenue
(ironic consequence). This one wins on an ironic consequence too, but
with a different artifact — a cached error page, not a billing bug.
The laugh word is last (shutap.com rule), and it is a specific,
drawable thing a stranger could picture: an error page.
"""

import os

JOKE = "My agent fixed the slow query by caching the error page."
# 56 characters, one line, no trailing newline: the punchline is
# "the error page" — a specific technical artifact at the very end,
# re-interpreting "fixed" as "made the error load fast".

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
