#!/usr/bin/env python
"""
Problem: Given a list of dict. How to write that list to a csv,
with header and deal with missing values.
"""
import csv
import io


def main():
    """Entry"""
    rows = [
        {"uid": 501, "alias": "peter", "shell": "zsh"},
        {"uid": 502, "alias": "paul", "shell": "bash"},
        {"uid": 502, "alias": "mary"},
    ]

    headers = {}
    for row in rows:
        headers.update(row)

    with io.StringIO() as buffer:
        writer = csv.DictWriter(buffer, headers)
        writer.writeheader()
        writer.writerows(rows)
        print(buffer.getvalue())


if __name__ == "__main__":
    main()
