#!/usr/bin/env python
# encoding: utf-8

"""
Unpack is nice, but the name of the tests are awful.
"""

import unittest
import ddt

test_data = [
    dict(container="story1",  a=1, b=2),
    dict(container="dashboard2", a=4, b=5),
]


@ddt.ddt
class UnpackTest(unittest.TestCase):
    @ddt.data(*test_data)
    @ddt.unpack
    def test1(self, container, b, a):
        print 'container={}, a={}, b={}'.format(container, a, b)


if __name__ == '__main__':
    unittest.main()
