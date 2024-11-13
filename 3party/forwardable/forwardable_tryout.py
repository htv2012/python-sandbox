#!/usr/bin/env python3
from forwardable import def_delegators, forwardable


@forwardable()
class MySet:
    def_delegators("_data", "add,discard,__len__")

    def __init__(self):
        self._data = set()


def main():
    """Entry"""

    ms = MySet()
    assert len(ms) == 0
    ms.add("foo")
    assert len(ms) == 1
    ms.add("bar")
    assert len(ms) == 2
    ms.discard("foo")
    assert ms._data == {"bar"}


if __name__ == "__main__":
    main()
