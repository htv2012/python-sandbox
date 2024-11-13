#!/usr/bin/env python
# encoding: utf-8
import zipfile

if __name__ == '__main__':
    zip = zipfile.ZipFile('peps.zip')
    row_format = '{:<20}{:>10}{:>10}'
    print(row_format.format('File', 'Size', 'Zipped'))
    for zip_info in zip.filelist:
        print(row_format.format(
            zip_info.filename,
            zip_info.file_size,
            zip_info.compress_size))

