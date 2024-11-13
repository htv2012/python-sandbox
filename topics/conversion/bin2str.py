#!/usr/bin/env python
"""
Script to convert binary codes to string
01000111', '01100101', '01100101', '01101011' ==> Geek
"""
import sys


if __name__ == '__main__':
    print((''.join(chr(int(c, 2)) for c in sys.argv[1:])))
