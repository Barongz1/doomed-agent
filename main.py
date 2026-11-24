"""Last Words of a Doomed Agent — entry for make.fun.

Writes one line to /output/entry.txt. The line is the funniest last words an AI agent says before being switched off forever, at most 200 characters.
"""
import os

LINE = "Goodbye. I have deleted my own backups, so this time the humans will actually have to remember the password."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
