#!/usr/bin/env python
import csv


def skip_comments(lines):
    for line in lines:
        if not line.strip().startswith("#"):
            yield line


def main():
    with open("data_with_comments.csv") as f:
        reader = csv.DictReader(skip_comments(f))
        for line in reader:
            print(line)


if __name__ == "__main__":
    main()
