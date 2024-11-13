#!/usr/bin/env python


import os
import sys
import imp


def parent_package_from_module_name(module_name):
    if '.' in module_name:
        return '.'.join(module_name.split('.')[:-1])
    else:
        return ''


def tryout(module_name):
    package = parent_package_from_module_name(module_name)
    print(module_name, '==>', package)


def main():
    tryout('re')
    tryout('atom.desktop')
    tryout('atom.atom_logger')
    tryout('atom')
    tryout('atom.action_layer')
    tryout('atom.action_layer.desktop.common')
    tryout('atom.action_layer.desktop.common.common_action')


if __name__ == '__main__':
    main()
