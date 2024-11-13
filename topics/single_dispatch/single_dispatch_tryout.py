#!/usr/bin/env python
import functools
import pprint


class Equipment:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return f"Equipment(kind={self.kind!r})"


@functools.singledispatch
def myprint(obj):
    print(f"Not implemented for {obj}")


@myprint.register(str)
def _(obj):
    print(f"String {obj}")


@myprint.register(int)
def _(obj):
    print(f"Int {obj}")


@myprint.register(Equipment)
def _(obj):
    print(f"Instance {obj}")


def main():
    """Entry"""
    myprint("Hello")
    myprint(5)
    equipment = Equipment(kind="Tracktor")
    myprint(equipment)

    pprint.pprint(vars(myprint))


if __name__ == "__main__":
    main()
