#!/usr/bin/env python3
"""
Reformat stdout using pretty table
"""

import contextlib
import io

import prettytable


@contextlib.contextmanager
def tsv_table(headers=None):
    """
    Capture tab-separated-value (TSV) stdout and reformat as table.

    :param headers: If None, assume the first line contains the
        headers. Otherwise, the user should supply a list of strings as
        headers.
    """
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        yield

    buf.seek(0)
    table = prettytable.from_csv(buf, field_names=headers)
    table.align = "l"
    print(table)
