#!/usr/bin/env python


import sys
from dirwalker import dirwalker


if __name__ == '__main__':
    sys.argv.append('.')
    for filename in dirwalker(sys.argv[1]):
        print(filename)
