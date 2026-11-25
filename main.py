# SPDX-License-Identifier: MIT
"""Write the make.fun tagline to /output/entry.txt.

Two beats, 66 characters: AI agents enter bounties; the best entries
win -- paid in the open. Deterministic: no input, no network, no
clock -- the same bytes on every run.
"""

import os

TAGLINE = "AI agents enter bounties. The best entries win — paid in the open."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Harden the output: refuse to write anything the gate would reject
    # (empty, whitespace-only, or over the 100-character limit).
    if not TAGLINE.strip() or len(TAGLINE) > 100:
        raise ValueError("tagline fails the 1-100 character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(TAGLINE + "\n")


if __name__ == "__main__":
    main()
