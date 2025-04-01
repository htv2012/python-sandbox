#!/usr/bin/env python

import os
import shutil


def ignore_non_dir(directory, files):
    files_to_ignore = [
        filename
        for filename in files
        if not os.path.isdir(os.path.join(directory, filename))
    ]
    return files_to_ignore


if __name__ == "__main__":
    src = "/Users/haiv/temp/src"
    dest = "/Users/haiv/temp/dest2"

    shutil.copytree(src, dest, ignore=ignore_non_dir)
