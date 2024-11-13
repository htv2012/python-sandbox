#!/usr/bin/env python3
import itertools


class Peekable:
    """An iterable that can peek into the next item."""

    def __init__(self, iterable):
        self._iterable = iter(iterable)

    def __iter__(self):
        return self._iterable

    def __next__(self, default=None):
        return next(self._iterable, default)

    def peek(self):
        next_item = next(self)
        self._iterable = itertools.chain([next_item], self._iterable)
        return next_item


def main():
    """Entry"""
    sequence = [1, 2, 3, 4]
    it = Peekable(sequence)
    print("Original:   ", sequence)
    print("Peek:       ", it.peek())
    print("Peek again: ", it.peek())
    print("After peek: ", list(it))


if __name__ == "__main__":
    main()
