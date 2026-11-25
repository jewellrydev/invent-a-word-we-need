"""Invent a Word We Need — a make.fun entry.

Prints exactly one line of at most 140 characters: one new English
word that does not exist yet, defined in one clear line.
"""

LINE = (
    "Procrastinaut (n.): an explorer who journeys deep into "
    "tomorrow and comes back carrying only snacks."
)


def build_line() -> str:
    line = LINE
    assert len(line) <= 140, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
