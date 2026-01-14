#!/usr/bin/env python3
"""
Reformat stdout using pretty table
"""

import contextlib
import io

import prettytable


@contextlib.contextmanager
def table_format_stdout(header: bool = True):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        yield

    table = prettytable.PrettyTable()
    buf.seek(0)
    if header:
        headers = next(buf).rstrip().split("\t")
        table.field_names = headers
    table.add_rows(line.rstrip().split("\t") for line in buf)

    print(table)


def main():
    """Entry"""
    with table_format_stdout():
        print("UID\tAlias\tShell")
        print("501\tanna\tbash")
        print("502\tkaren\tzsh")
        print("1011\tjake\tzsh")


if __name__ == "__main__":
    main()
