#!/usr/bin/env python3
"""Create CSV from fileinput."""

import csv
import fileinput


def main():
    """Entry"""
    reader = csv.reader(fileinput.input())
    for row in reader:
        print(row)


if __name__ == "__main__":
    main()
