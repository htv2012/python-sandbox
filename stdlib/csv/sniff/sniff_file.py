#!/usr/bin/env python3
"""Sniff text from a file to determine CSV dialect."""
import csv


def main():
    """Perform script."""
    with open("users.csv") as stream:
        # Read about 1KB of text and guess the CSV dialect
        dialect = csv.Sniffer().sniff(stream.read(1024))
        stream.seek(0)
        reader = csv.reader(stream, dialect=dialect)

        for row in reader:
            print(row)


if __name__ == "__main__":
    main()
