#!/usr/bin/env python3
"""
A Python skeleton script
"""

from get_attr import get_attr


class V1:
    def getData(self):
        return {"version": "1.0", "name": "getData"}


class V2:
    def get_data(self):
        return {"version": "2.0", "name": "get_data"}


class V3:
    @property
    def data(self):
        return {"version": "3.0", "name": "data"}


class Unrelated:
    def foo(self):
        pass

    def bar(self):
        pass


objects = [V1(), V2(), V3(), Unrelated()]
for obj in objects:
    print()
    print(f"# {obj.__class__.__name__} object")
    data = get_attr(obj, "getData", "get_data", "data")
    print(data)


def main():
    """Entry"""


if __name__ == "__main__":
    main()
