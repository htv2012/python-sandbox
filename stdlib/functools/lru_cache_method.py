#!/usr/bin/env python3
"""
whatis: See if lru_cache works for a method
"""
import functools


@functools.lru_cache
def double(n):
    print(f"{n} not found in cache, calculate it")
    return n * 2


def main():
    """Entry"""
    print("\n#\n# lru_cache demo\n#")

    n = 5
    print(f"\n# First call with {n=}")
    result = double(n)
    print(f"double({n}) ==> {result}")

    print(f"\n# Second call with {n=}")
    result = double(n)
    print(f"double({n}) ==> {result}")


if __name__ == "__main__":
    main()
