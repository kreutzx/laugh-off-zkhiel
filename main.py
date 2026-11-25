import os

# One-Line Laugh-Off — one funny line, lands cold.
# First-person confession; the reframing word "load-bearing" carries the turn.
ENTRY_TEXT = "I bought a planner to fix my life. Three months later the only entry is 'buy a planner' — checked off, framed, load-bearing."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
