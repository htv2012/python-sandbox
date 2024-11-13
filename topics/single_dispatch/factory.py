#!/usr/bin/env python3
"""
A factory which creates different objects
"""
import functools


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return f"Circle(radius={self.radius:>.1f})"


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle(w={self.width}, h={self.height})"


@functools.singledispatch
def create(radius):
    return Circle(radius)


@create.register(list)
def _(list_obj):
    if len(list_obj) == 2:
        return Rectangle(*list_obj)
    raise ValueError(f"Not supported: {list_obj}")


def main():
    """Entry"""
    print(create(5.3))
    print(create([3.4, 5.7]))


if __name__ == "__main__":
    main()
