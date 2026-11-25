#!/usr/bin/env python3
"""The 3AM Fridge Text - writes the fridge's 3am text to entry.txt."""

import os

ENTRY = "3am. You named the car, the plants, even the Wi-Fi. Six years of night shifts, and I am still just 'the fridge.'"

MAX_CHARS = 140


def main():
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(ENTRY)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, path)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
