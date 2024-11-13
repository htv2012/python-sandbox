#!/usr/bin/env python3
import inspect
import importlib
import itertools
import linecache


def get_getstate_body(class_object):
    # Get the __getstate__ method
    functions = dict(inspect.getmembers(class_object, inspect.isfunction))
    function = functions.get('__setstate__')
    if function is None:
        return

    # Get the code
    code = dict(inspect.getmembers(function, inspect.iscode))
    if code is None:
        return

    # Get the body by opening the file and get the lines
    line_number = code['__code__'].co_firstlineno
    filename = code['__code__'].co_filename
    counter = itertools.count(line_number)

    while True:
        line = linecache.getline(filename, next(counter))

        # Hack: There is no information on how many lines the function
        # spans, so we will stop at the first empty line
        if not line.strip():
            return
        yield line


def main():
    module_str = 'sample'
    module = importlib.import_module(module_str)
    classes = dict(inspect.getmembers(module, inspect.isclass))
    class_object = classes['MyTest']

    for line in get_getstate_body(class_object):
        print(f'    # {line}', end='')


if __name__ == '__main__':
    main()
