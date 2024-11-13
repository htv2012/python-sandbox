#!/usr/bin/env python3
"""Sniff text to determine CSV dialect."""
import csv


def main():
    """Perform script."""
    text = "501\tkaren\n502\tjohn"
    dialect = csv.Sniffer().sniff(text)

    reader = csv.reader(text.splitlines(), dialect=dialect)
    for row in reader:
        print(row)


if __name__ == "__main__":
    main()
