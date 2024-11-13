#!/usr/bin/env python
# encoding: utf-8
"""
skip_lines.py

Created by Hai Vu on 2013-02-23.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import csv


def skip_first(seq, n):
    for i, item in enumerate(seq):
        if i >= n:
            yield item


def main():
    with open("data.txt", "rb") as f:
        csvreader = csv.reader(f)
        for line in skip_first(csvreader, 4):
            print(line)

    # Can be used to skip any sequence, not just file
    list = ["happy", "grumpy", "doc", "sleepy", "bashful", "sneezy", "dopey"]
    for item in skip_first(list, 3):
        print(item)

    # A different way to skip first 4 lines
    with open("data.txt") as f:
        csvreader = csv.reader(f)
        all(next(csvreader) for i in range(4))
        for line in csvreader:
            print(line)


if __name__ == "__main__":
    main()
