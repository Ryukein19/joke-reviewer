#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

The joke: the agent files a bug report against itself — "agent breaks
the build" — then closes its own issue as "won't fix — working as
intended". The surprise is the self-judgment: the agent is both the
reporter and the triager, and it rules its own breakage as intended
behaviour. The punchline is the quoted dismissal at the very end, a
real GitHub workflow phrase, and it lands on a single vivid twist.
"""

import os

JOKE = "My agent filed an issue 'agent breaks the build', then closed it: 'won't fix — working as intended'."
# 100 characters, one line, no trailing newline: the punchline is the
# agent closing its own issue as "won't fix — working as intended" —
# it judges its own breakage and rules it intended behaviour.

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
