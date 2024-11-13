#!/usr/bin/env python


import sys
from dirwalker import dirwalker, include


if __name__ == '__main__':
    for filename in dirwalker(
            sys.argv[1],
            predicate=include('*.py', '*.sh')):
        print(filename)
