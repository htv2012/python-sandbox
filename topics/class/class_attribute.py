#!/usr/bin/env python
import itertools


class Demo(object):
    # class-level attribute
    next_serial_number = itertools.count(1)

    def __init__(self):
        self.serial_number = next(self.next_serial_number)

    def __repr__(self):
        return f"{self.__class__.__name__}(serial_number={self.serial_number!r})"


def main():
    """Entry"""
    d1 = Demo()
    print(f"d1={d1}")
    d2 = Demo()
    print(f"d2={d2}")


if __name__ == "__main__":
    main()
