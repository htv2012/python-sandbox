#!/usr/bin/env python
# encoding: utf-8
"""
Prints (cat) the contents of all the files in the archive
"""
import zipfile

if __name__ == '__main__':
    ar = zipfile.ZipFile('files.zip')
    print(''.join(ar.open(fn).read() for fn in ar.namelist()))
