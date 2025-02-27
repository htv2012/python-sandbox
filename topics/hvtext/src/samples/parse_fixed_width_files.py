#!/usr/bin/env python
"""
Demonstrate the use of split_rows with and without guessing
"""

import pathlib

from hvtext import fixed_width

DATA_PATH = pathlib.Path(__file__).with_name("table.txt")


def main():
    """Main entry"""
    # Supply the columns
    columns = [1, 19, 27, 36]
    with open(DATA_PATH) as file_handle:
        for row in fixed_width.split_rows(file_handle, columns):
            print(row)

    # Guess the columns
    print("---")
    with open(DATA_PATH) as file_handle:
        for row in fixed_width.split_rows(file_handle):
            print(row)


if __name__ == "__main__":
    main()
