#!/usr/bin/env python3
"""Demo the Callable as aid to IDE."""
from typing import Callable

Predicate = Callable[[int], bool]
Vector = list[int]

def select(seq: Vector, predicate: Predicate) -> Vector:
    out = [elem for elem in seq if predicate(elem)]
    return out


def is_odd(num: int) -> bool:
    return num % 2 == 1


def main():
    """Entry"""
    print(select([1, 2, 3, 4, 5], is_odd))


if __name__ == "__main__":
    main()
