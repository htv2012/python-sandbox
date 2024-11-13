#!/usr/bin/env python3
"""Convert a multi-line string to CSV rows."""

import csv
from io import StringIO


def main():
    """Entry"""
    buffer = """
    id,alias,shell
    501,haiv,bash
    502,tracyv,csh
    """.strip()

    # First method: splitlines
    reader = csv.reader(buffer.splitlines())
    for row in reader:
        print(row)

    print("---")

    # Second method: using StringIO
    reader = csv.reader(StringIO(buffer))
    for row in reader:
        print(row)


if __name__ == "__main__":
    main()
