#!/usr/bin/env python
"""
Demo: Skip blank and comments in CSV
"""
import csv
import pathlib

from hvtext import discard


def main():
    """ Entry """
    data_path = pathlib.Path(__file__).with_name('csv_with_comments.csv')
    with open(data_path) as csv_file:
        csv_file = discard.comment(csv_file)
        csv_file = discard.blank(csv_file)
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            print(row)


if __name__ == '__main__':
    main()

