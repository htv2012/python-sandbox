#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys


class Const(object):
    def __init__(self):
        self._d = dict()

    def __setattribute__(self, name, value):
        print('>>>', name, '=', value)
        inner_dict = super(Const, self).__getattribute__('__dict__')
        if inner_dict.setdefault(name, value) != value:
            raise AttributeError('Cannot redefine constant')

    # def __set__(self, name, value):
    #     new_value = self._d.setdefault(name, value)
    #     print('>>> new:', new_value)
    #     if new_value != value:
    #         raise AttributeError('Cannot override constant')

    # def __get__(self, name, type=None):
    #     print('>>> get:', name)
    #     try:
    #         return self._d[name]
    #     except KeyError:
    #         raise AttributeError('Constant not found: {}'.format(name))

if __name__ == '__main__':
    color = Const()
    color.red = 1
    print('red is:', color.red)
    color.red = 1
    color.red = 2
    print('red is:', color.red)
