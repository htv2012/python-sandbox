#!/usr/bin/env python
"""
Archives a directory: ~/myenv to /tmp/myenv.tar.bz2
"""
import pathlib
import shutil


archive_name = shutil.make_archive(
    base_name="/tmp/myenv",
    format="bztar",
    root_dir=pathlib.Path.home(),
    base_dir="myenv",
)
print(f"Archived to: {archive_name}")
