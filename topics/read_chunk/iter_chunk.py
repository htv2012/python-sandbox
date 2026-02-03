#!/usr/bin/env python3
"""
Split up a sequence into chunks
"""

from collections.abc import Sequence


def iter_chunk(data: Sequence, chunk_size: int):
    """Split a sequence into chunks, each of chunk_size in length."""
    i = 0
    limit = len(data)

    while i < limit:
        yield data[i : i + chunk_size]
        i += chunk_size


def tryout(data: Sequence):
    print()
    print("#")
    print(f"# {data = }")
    print("#")

    for chunk_size in [3, 4, 5, 20]:
        print(f"\n# {chunk_size = }")
        for chunk in iter_chunk(data, chunk_size):
            print(f"length = {len(chunk)}, {chunk = }")

def main():
    """Entry"""
    tryout("0123456789")
    tryout(list(range(10)))


if __name__ == "__main__":
    main()
