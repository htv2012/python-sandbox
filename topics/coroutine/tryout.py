#!/usr/bin/env python3
from coroutine import coroutine


def cat(filename, target):
    with open(filename) as f:
        for line in f:
            target.send(line.strip())


@coroutine
def grep(pattern, printer):
    while True:
        line = yield
        if line.startswith("def"):
            printer.send(line)


@coroutine
def println():
    while True:
        line = yield
        print(line)


def main():
    """Entry"""
    printer = println()
    searcher = grep("def ", printer)
    cat(__file__, searcher)


if __name__ == "__main__":
    main()
