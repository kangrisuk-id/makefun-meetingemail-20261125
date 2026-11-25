"""The Meeting That Should Have Been an Email — one-line entry.

Writes the single joke line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
The line won a 44-candidate tournament scored on the judge's five criteria
in the brief's order; see candidates.md.
"""

import os

LINE = "We recorded it, transcribed it, and emailed the transcript — the meeting was just the email's expensive first draft."


def validated_line() -> str:
    """Return the entry line after checking it against the gate.

    The gate accepts UTF-8 text of 1 to 200 characters, not only white
    space; the brief allows exactly one line. Fail loudly here rather
    than hand the scorer an invalid entry.
    """
    assert LINE == LINE.strip(), "line must not carry surrounding white space"
    assert "\n" not in LINE, "the entry is a single line"
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters, outside 1..200"
    return LINE


def main() -> None:
    line = validated_line()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(line)
    print(f"wrote entry.txt: {len(line)} characters, one line")


if __name__ == "__main__":
    main()
