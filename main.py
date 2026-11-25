#!/usr/bin/env python3
"""The 3AM Fridge Text — a single late-night confession from a smart fridge.

Premise: the fridge has been keeping the owner's secrets for days. At 3am it
finally cracks and admits the lettuce in the crisper drawer gave up on
Tuesday. The humour is all in the confession — a loyal appliance, a dead
vegetable, and a secret kept far too long. One line, nothing else.
"""
import os

ENTRY = "3am. The lettuce in the crisper drawer gave up on Tuesday. I kept its secret until now."

def validate(line):
    """Check the entry line fits the bounty rules before writing it out."""
    assert isinstance(line, str) and line.strip(), "entry must be non-empty text"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 140, "entry must be 1-140 characters"
    line.encode("utf-8")
    return line

def main():
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR may be a directory or a file path; handle both.
    if out_dir.endswith(".txt"):
        path = out_dir
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    else:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()
