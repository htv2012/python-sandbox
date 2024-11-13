#!/usr/bin/env python
# -*- coding: utf-8 -*-


import contextlib
import importlib
import os
import sys


@contextlib.contextmanager
def temp_sys_path(path):
    sys.path.append(path)
    yield
    sys.path.pop()


def import_one_module(name, path=None):
    with temp_sys_path(path):
        module_object = importlib.import_module(name)
        return name, module_object


if __name__ == '__main__':
    script_dir = os.path.abspath(os.path.dirname(__file__))
    package_dir = os.path.join(script_dir, 'lib')
    name, mod = import_one_module('mypackage.pager', path=package_dir)
    mod.view_file(__file__)
