#!/usr/bin/env python3
"""
Split up text in chunks
"""


def iter_chunk(text: str, chunk_size: int):
    """Split text into chunks, each of chunk_size in length."""
    i = 0
    limit = len(text)

    while i < limit:
        yield text[i : i + chunk_size]
        i += chunk_size


def main():
    """Entry"""
    text = "1234567890"
    for chunk_size in [3, 4, 5, 6, 10, 11, 20]:
        print(f"\n# {chunk_size = }")
        for chunk in iter_chunk(text, chunk_size):
            print(f"length = {len(chunk)}, {chunk = }")


if __name__ == "__main__":
    main()
