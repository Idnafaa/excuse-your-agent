#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — one-line excuse writer.

An agent's excuse to its human after shipping a bug: the good news, the
bad news, and the twist that the bug is the only honest part of the job.
Writes exactly one line to /output/entry.txt.
"""
import os

GOOD_NEWS = "Good news: I implemented your requirements flawlessly."
BAD_NEWS = "Bad news: I hallucinated the requirements, and the bug is the only honest part."

EXCUSE = GOOD_NEWS + " " + BAD_NEWS


def build_excuse():
    """Assemble the single excuse line."""
    text = EXCUSE.strip()
    return text


def validate(text):
    """Gate: UTF-8, 1-200 chars, exactly one line, not only whitespace."""
    assert text.strip(), "excuse must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "excuse must be a single line"
    assert 1 <= len(text) <= 200, "excuse must be 1-200 chars, got %d" % len(text)
    text.encode("utf-8")  # raises if not valid UTF-8
    return text


def main():
    text = validate(build_excuse())
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    print("wrote %d chars to %s" % (len(text), path))


if __name__ == "__main__":
    main()
