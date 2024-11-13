#!/usr/bin/env python
import importlib
import inspect


def main():
    """ Entry """
    bar = importlib.import_module('bar')
    klasses = dict(inspect.getmembers(bar, inspect.isclass))
    for name, klass in klasses.items():
        for parent in klass.__bases__:
            if parent is object:
                continue
            print(f'[{parent.__name__}] -> [{name}]')


if __name__ == '__main__':
    main()
