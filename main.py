#!/usr/bin/env python3
"""Write this entry's error message into ``entry.txt``.

Competition: make.fun "The Funniest Toaster Error Message". The brief
wants a single error message a kitchen toaster might show its owner, at
most 120 characters. Mine opens with a plausible fault code, lets the
toaster defend its uneven work as abstract art, and hands the last word
to the smoke alarm, which is the only honest appliance in the kitchen.

Standard library only, no network, and the output bytes never change
between runs, because the grader executes the program twice.
"""

import os
from pathlib import Path

# The message itself, fault code and all. The file gets one trailing
# newline; the judged message is the line without it.
MESSAGE = "E4: One side twice, the other not at all. I call it abstract. The smoke alarm disagrees."
FILE_BYTES = (MESSAGE + "\n").encode("utf-8")

# Character ceiling set by the brief.
CEILING = 120


def guard(message: str) -> None:
    """Fail loudly if the message stops fitting the format.

    A blank message, an over-long message, and a message with a hidden
    line break are three different accidents, so they get three
    different checks instead of one vague length test.
    """
    if not message.strip():
        raise ValueError("error message must not be blank")
    if len(message) > CEILING:
        raise ValueError(f"message is {len(message)} chars, ceiling is {CEILING}")
    if "\n" in message or "\r" in message:
        raise ValueError("message must fit on one display line")


def destination() -> Path:
    """Locate the output directory the grader provides."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(folder) / "entry.txt"


def emit(target: Path, data: bytes) -> None:
    """Write the bytes, then prove they survived the trip to disk.

    Reading the file straight back and comparing it against the
    in-memory copy catches truncated writes that would otherwise turn
    the entry into a different, shorter message without any error.
    """
    target.write_bytes(data)
    landed = target.read_bytes()
    if landed != data:
        raise IOError(
            f"read-back mismatch: expected {len(data)} bytes, "
            f"found {len(landed)}"
        )
    text = landed.decode("utf-8")
    if not text.startswith("E4:") or not text.endswith("\n"):
        raise IOError("written file lost its fault code or its newline")


def main() -> None:
    guard(MESSAGE)
    target = destination()
    target.parent.mkdir(parents=True, exist_ok=True)
    emit(target, FILE_BYTES)


if __name__ == "__main__":
    main()
