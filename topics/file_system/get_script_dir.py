#!/usr/bin/env python
"""
Robust way to get the script directory
http://stackoverflow.com/a/22881871/459745
"""

import inspect
import os
import sys


def get_script_dir(follow_symlinks=True):
    if getattr(sys, "frozen", False):  # py2exe, PyInstaller, cx_Freeze
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)


print(get_script_dir())
