#!/usr/bin/env python3
"""
Use the greet.zip
"""

from farewell import bye
from greet import greet


def main():
    """Entry"""
    greet("world")
    bye("world")


if __name__ == "__main__":
    main()
