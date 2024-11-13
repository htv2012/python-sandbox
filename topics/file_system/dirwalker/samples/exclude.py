#!/usr/bin/env python


import sys
from dirwalker import dirwalker, exclude


if __name__ == '__main__':
    for filename in dirwalker(sys.argv[1], predicate=exclude(*sys.argv[2:])):
        print(filename)
