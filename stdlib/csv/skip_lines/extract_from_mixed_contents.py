"""
whatis: Extract a specific CSV table from a report

https://stackoverflow.com/q/57095143/459745
"""

import csv
from itertools import dropwhile, takewhile


def main():
    """Entry"""
    header = "Device Name,Number"

    with open("report.txt") as fh:
        fh = dropwhile(lambda line: header not in line, fh)
        fh = takewhile(lambda line: line != "\n", fh)
        reader = csv.reader(fh)
        for row in reader:
            print(row)


if __name__ == "__main__":
    main()
