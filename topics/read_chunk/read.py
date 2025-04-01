#!/usr/bin/env python
"""Read a file in chunks"""

if __name__ == "__main__":
    CHUNK_SIZE = 40
    with open("data.txt") as f:
        for chunk in iter(lambda: f.read(CHUNK_SIZE), ""):
            print("{!r}".format(chunk))
