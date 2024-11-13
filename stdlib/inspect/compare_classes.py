#!/usr/bin/env python


import inspect
import imp
import os

def get_files(dir, predicate=None):
    """ Generator to return files from a directory that matches a predicate
    :param dir:
    :param predicate:
    :return:
    """
    for filename in os.listdir(dir):
        if predicate is None or predicate(filename):
            # yield dict(filename=filename, dir=dir)
            yield filename


def compare_files(dira, dirb, predicate=None):
    filesa = frozenset(get_files(dira, predicate))
    filesb = frozenset(get_files(dirb, predicate))
    only_in_a = filesa - filesb
    only_in_b = filesb - filesa
    common = filesa & filesb
    return only_in_a, common, only_in_b


def print_files_set(files_set, label):
    print('=' * 60)
    print(label)
    print('=' * 60)
    for filename in sorted(files_set):
        print('-', filename)
    print('')


def get_classes(filename, dir):
    module_name = os.path.splitext(filename)[0]
    file_handle, pathname, description = imp.find_module(module_name,[dir])
    mod = imp.load_module(module_name, file_handle, pathname, description)
    classes = frozenset(inspect.getmembers(mod, inspect.isclass))
    return classes


def compare_classes(old_dir, new_dir, files_set):
    for filename in sorted(files_set):
        old_classes = get_classes(filename, old_dir)
        new_classes = get_classes(filename, new_dir)


if __name__ == '__main__':
    is_python_module = lambda filename: filename.endswith('.py') and filename != '__init__.py'
    to_be_added, common, to_be_removed = compare_files('new', 'old', is_python_module)
    print_files_set(to_be_added, 'To be added')
    print_files_set(common, 'Common')
    print_files_set(to_be_removed, 'To be removed')

    compare_classes('old', 'new', common)
