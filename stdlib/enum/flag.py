#!/usr/bin/env python3
"""
whatis: Example of enum.Flag
"""

from enum import Flag, auto


class Fault(Flag):
    CONNECTION_ERROR = auto()
    BAD_CREDENTIALS = auto()
    INVALID_TOKEN = auto()


def main():
    """Entry"""
    fault = Fault.BAD_CREDENTIALS | Fault.INVALID_TOKEN
    print(f"{fault = }")
    print(f"{Fault.INVALID_TOKEN in fault = }")
    print(f"{Fault.CONNECTION_ERROR in fault = }")


if __name__ == "__main__":
    main()
