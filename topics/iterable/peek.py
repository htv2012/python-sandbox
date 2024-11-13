#!/usr/bin/env python3
"""How to peek into an interable."""
import itertools


def main():
    """Entry"""
    seq = [1, 2, 3]
    print(f"Original:       {seq}")

    # Peek into the iterable by creating a duplicate
    seq, dup_of_seq = itertools.tee(seq)
    print(f"Peek and found: {next(dup_of_seq)}")

    # Print the iterable it to show that peek does not change it
    print(f"After peeking:  {list(seq)}")


if __name__ == "__main__":
    main()
