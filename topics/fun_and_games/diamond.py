#!/usr/bin/env python3
"""
Given a number, say 5 prints a diamond:
    1
   121
  12321
 1234321
123454321
 1234321
  12321
   121
    1
"""


def make_row(size, width):
    buf = ""
    for i in range(1, size + 1):
        buf += str(i)
    for i in range(size - 1, 0, -1):
        buf += str(i)
    return buf.center(width)


def diamond(size):
    width = size * 2 - 1
    stack = []
    for row_number in range(1, size):
        row = make_row(row_number, width)
        print(row)
        stack.append(row)

    stack.pop()
    stack.reverse()
    for row in stack:
        print(row)


def main():
    """ Entry """
    diamond(6)



if __name__ == '__main__':
    main()
