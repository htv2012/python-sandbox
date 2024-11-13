#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import ddt
import logging
import unittest


logging.basicConfig(level=logging.DEBUG)
logger = logging
test_cases = {
    'case1': dict(a=1, b=2),
    'case2': dict(a=3, b=4),
}


@ddt.ddt
class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logger.info('setUpClass')

    def setUp(self):
        logger.info('setUp')

    @ddt.data(*test_cases)
    def test1(self, key):
        test_info = test_cases[key]

        logger.info('test1, %s', self.id().split('.')[-1])
        logger.info('key={1}, a={0[a]}, b={0[b]}'.format(test_info, key))

if __name__ == '__main__':
    unittest.main()
