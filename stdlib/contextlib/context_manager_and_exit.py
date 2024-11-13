#!/usr/bin/env python3
"""Does context manager got clean up when exit?"""
import contextlib
import sys


@contextlib.contextmanager
def mycontext():
    print("before")
    try:
        yield
    finally:
        print("after")


def main():
    """Entry"""
    with mycontext():
        print("inside")
        sys.exit(0)


if __name__ == "__main__":
    main()
