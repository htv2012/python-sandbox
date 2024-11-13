#!/usr/bin/env python3
"""
Demo: Use tabulate to display CSV
"""
import csv
import pathlib

import tabulate


def main():
    """Entry"""
    data_path = pathlib.Path(__file__).with_name("users.csv")
    with open(data_path) as stream:
        reader = csv.reader(stream)
        print(tabulate.tabulate(reader, headers="firstrow", tablefmt="github"))


if __name__ == "__main__":
    main()
