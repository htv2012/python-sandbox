#!/usr/bin/env python
"""
A way to view text or file via the system's pager.

"""

import os
import subprocess


def _get_pager(pager_executable: str = None):
    """
    Returns the name of the system pager, which is default to less and
    can be overriden by setting the environment variable PAGER.
    """
    return pager_executable or os.getenv("PAGER", "less")


def view_text(text, pager=None):
    """
    Use the system pager to view a (large) piece of text. If the system
    environment variable PAGER exists, it will be used. Otherwise,
    less will be used.
    """
    pager_executable = _get_pager(pager)
    pager_process = subprocess.Popen(
        pager_executable,
        stdin=subprocess.PIPE,
        encoding="utf-8",
    )
    with pager_process:
        pager_process.stdin.write(text)
        pager_process.stdin.close()
        pager_process.wait()


def view_file(filename, pager=None):
    """
    Use the system pager to view a file. If the system environment
    variable PAGER exists, it will be used. Otherwise, less will be
    used.

    view_file() returns True on success, False otherwise.
    """
    cmd = [_get_pager(pager), filename]
    return subprocess.call(cmd) == 0
