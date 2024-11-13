#!/usr/bin/env python3
""" CSV to interpret cells without quote as numeric """
import csv
import io


def main():
    """ Entry """
    buffer = io.StringIO()
    rows = [
        ["uid", "alias"],
        [501, "peter"],
        [502, "paul"],
        [503, "mary"],
    ]

    # Writes and verifies that non-numeric cells get quoted
    writer = csv.writer(buffer, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerows(rows)
    print("\nContents of CSV:")
    print(buffer.getvalue())

    # Reads and verifies that data got converted to numeric (float)
    print("\nRead result:")
    buffer.seek(0)
    reader = csv.reader(buffer, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)


if __name__ == "__main__":
    main()
