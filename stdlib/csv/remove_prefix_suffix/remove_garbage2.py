#!/usr/bin/env python

""" Remove garbage from a line before passing it to the CSV reader """



import csv


def remove_garbage(iterable):
    for line in iterable:
        line = line.lstrip('|').rstrip('|\n')
        yield line


def main():
    with open('data.csv') as f:
        reader = csv.reader(remove_garbage(f))
        for row in reader:
            print(row)


if __name__ == '__main__':
    main()
