#!/usr/bin/env python3
"""
Unpack an archive using zipfile
"""

import zipfile

with zipfile.ZipFile("my.zip") as zip:
    for name in zip.namelist():
        zip.extract(name, path="out")
