#!/usr/bin/env python

import os
import re


def build_files_set(rootdir):
    root_to_subtract = re.compile(r'^.*?' + rootdir + '[\\/]{0,1}')
    files_set = set()
    for (dirpath, dirnames, filenames) in os.walk(rootdir):
        for filename in filenames + dirnames:
            full_path = os.path.join(dirpath, filename)
            relative_path = root_to_subtract.sub('', full_path, count=1)
            files_set.add(relative_path)

    return files_set


def compare_directories(dir1, dir2):
    files_set1 = build_files_set(dir1)
    files_set2 = build_files_set(dir2)
    return (files_set1 - files_set2, files_set2 - files_set1)

if __name__ == '__main__':
    dir1 = 'old'
    dir2 = 'new'
    in_dir1, in_dir2 = compare_directories(dir1, dir2)

    print('\nFiles only in {}:'.format(dir1))
    for relative_path in sorted(in_dir1):
        print('* {0}'.format(relative_path))

    print('\nFiles only in {}:'.format(dir2))
    for relative_path in sorted(in_dir2):
        print('* {0}'.format(relative_path))
