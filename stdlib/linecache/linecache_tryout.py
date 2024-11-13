#!/usr/bin/env python3

import linecache


def main():
    """Entry"""
    for line_number in [1, 981, 412]:
        line = linecache.getline("msg.txt", line_number)
        print(line.rstrip())


if __name__ == "__main__":
    main()
