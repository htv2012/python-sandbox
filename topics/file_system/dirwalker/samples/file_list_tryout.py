#!/usr/bin/env python

from file_list import FileList


def show_cache(fullpath):
    print('----------------------------- Caching {}'.format(fullpath))


if __name__ == '__main__':
    root = '.'
    files = FileList(root)
    files.caching_hook = show_cache
    for filename in files:
        print(filename)

    print('No cache this time')
    for filename in files:
        print(filename)
