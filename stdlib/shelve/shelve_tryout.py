#!/usr/bin/env python
"""
whatis: Try out shelve
"""
import shelve
import tempfile


def main():
    with tempfile.NamedTemporaryFile(prefix='shelve_') as file_handle:
        filename = file_handle.name
    print(f'Shelve file: {filename}')

    with shelve.open(filename) as d:
        d['person'] = dict(alias='jamesk', uid=501)

    with shelve.open(filename) as d:
        person = d['person']
        print(f'Person: {person}')


if __name__ == '__main__':
    main()
