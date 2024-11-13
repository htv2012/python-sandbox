#!/usr/bin/env python3
"""
Use the greet.zip
"""
from greet import greet
from farewell import bye


def main():
    """ Entry """
    greet("world")
    bye("world")


if __name__ == "__main__":
    main()

