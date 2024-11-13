#!/usr/bin/env python3
"""Convert a stdin to CSV rows."""

import csv
import sys


def main():
    """Entry"""
    reader = csv.reader(sys.stdin)
    for row in reader:
        print(row)


if __name__ == "__main__":
    main()
