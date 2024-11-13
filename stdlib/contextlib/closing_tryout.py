#!/usr/bin/env python
"""
Demo: Automatically call close() using contextlib.closing()
"""
import contextlib


class MyObject:
    def close(self):
        print("close")

    def greet(self, name):
        print(f"Hello, {name}")


def main():
    my_object = MyObject()
    with contextlib.closing(my_object):
        my_object.greet("world")


if __name__ == "__main__":
    main()
