#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import inspect
import logging
import logging.config
import unittest


logging.config.fileConfig('logging.ini')
logger = logging.getLogger('name_of_tests')


class NameOfTests(unittest.TestCase):
    def test_get_name_using_inspect(self):
        self.inspect_helper()

    def test_get_name_using_id(self):
        self.id_helper()

    def inspect_helper(self):
        logger.info('Inspect Caller: %s', inspect.stack()[1][3])

    def id_helper(self):
        logger.info('ID Caller: %s', self.id())


if __name__ == '__main__':
    unittest.main()
