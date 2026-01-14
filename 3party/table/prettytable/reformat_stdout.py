#!/usr/bin/env python3
"""
Reformat stdout using pretty table
"""

import contextlib
import io

import prettytable


@contextlib.contextmanager
def table_format_stdout(headers=None):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        yield

    buf.seek(0)
    table = prettytable.from_csv(buf, field_names=headers)
    table.align = "l"
    print(table)


def main():
    """Entry"""
    with table_format_stdout():
        print("UID\tAlias\tShell")
        print("501\tanna\tbash")
        print("502\tkaren\tzsh")
        print("1011\tjake\tzsh")

    with table_format_stdout(headers=["User ID", "User Alias", "Shell"]):
        print("501\tanna\tbash")
        print("502\tkaren\tzsh")
        print("1011\tjake\tzsh")


if __name__ == "__main__":
    main()
