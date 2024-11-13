#!/usr/bin/env python

from collections import deque
from functools import partialmethod


class Stack(deque):
    """ A stack implemented using deque """
    push = deque.append

def main():
    """ Entry """
    stack = Stack([1, 2, 3, 4])
    stack.push(5)
    print('Stack:', stack)
    while stack:
        print(f"Pop -> {stack.pop()}")

if __name__ == '__main__':
    main()
