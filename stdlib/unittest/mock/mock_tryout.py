#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import mock


class Foo(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Foo({!r})'.format(self.name)

    def greet(self, name):
        print('Hello,', name)

if __name__ == '__main__':
    foo = Foo('bar')
    print('foo object:', foo)

    foo.greet = mock.MagicMock(name='greet')
    foo.greet('world')
    foo.greet.assert_called_once_with('world')
