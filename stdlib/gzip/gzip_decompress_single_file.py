#!/usr/bin/env python
# encoding: utf-8
"""
gzip_decompress_single_file.py

Created by Hai Vu on 2013-03-11.
Copyright (c) 2013 High View Software. All rights reserved.
"""

import sys
import os
import gzip


if __name__ == '__main__':
    infilename  = 'change_load_names.py.gz'
    outfilename = 'change_load_names.py'

    # Delete old file
    try:
        os.unlink(outfilename)
    except OSError:
        pass # Ignore case when file does not exist

    # Uncompress
    with open(outfilename, 'wb') as outfile, \
            gzip.open(infilename, 'rb') as infile:
        outfile.writelines(infile)


