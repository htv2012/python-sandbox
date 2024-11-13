#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import os
import sys
from collections import namedtuple
import unittest
import ddt


TestInfo = namedtuple('TestInfo', 'name workbook worksheet')


@ddt.ddt
class NamedTupleAsTestData(unittest.TestCase):
    test_data = [
        TestInfo('foo', 'workbook1.twbx', 'Sheet 1'),
    ]

    @ddt.data(*test_data)
    def test1(self, tc):
        self.assertTrue(tc.workbook.endswith('.twb'),
            'Invalid workbook: {}'.format(tc.workbook))


if __name__ == '__main__':
    unittest.main()
