#!/usr/bin/env python

""" Remove garbage from a line before passing it to the CSV reader """



import csv


def remove_garbage(filename):
    for line in open(filename):
        line = line.lstrip('|').rstrip('|\n')
        yield line


def main():
    for row in csv.DictReader(remove_garbage('data.csv')):
        print(row)


if __name__ == '__main__':
    main()
