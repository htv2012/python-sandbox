#!/usr/bin/env python
from typed_input import float_input, int_input

if __name__ == "__main__":
    value = int_input("Int Value: ")
    print("Value is {}".format(value))

    value = float_input("Float: ")
    print("Value is", value)
