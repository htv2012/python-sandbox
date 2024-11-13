#!/usr/bin/env python
"""
Extract not all file, but only specific ones
"""

import os
import zipfile

if __name__ == '__main__':
    DESTINATION = os.path.join(os.path.dirname(__file__), 'temp')

    archive = zipfile.ZipFile('drop_lines.twbx')
    for filename in archive.namelist():
        if filename.endswith('twb'):
            print('Extract {} to {}'.format(filename, DESTINATION))
            archive.extract(filename, DESTINATION)
