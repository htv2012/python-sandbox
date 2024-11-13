#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
from coroutine import coroutine


@coroutine
def line_printer(line_number=1):
    while True:
        line = yield
        print('{:>4} {}'.format(line_number, line))
        line_number += 1


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        printer = line_printer()
        for line in f:
            printer.send(line.rstrip())
