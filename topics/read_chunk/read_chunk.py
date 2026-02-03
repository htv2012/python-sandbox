#!/usr/bin/env python
"""Read a file in chunks"""


def main():
    chunk_size = 60
    with open("data.txt") as f:
        for chunk in iter(lambda: f.read(chunk_size), ""):
            print(f"length = {len(chunk)}, {chunk = }")


if __name__ == "__main__":
    main()
