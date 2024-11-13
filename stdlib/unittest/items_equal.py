#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import logging.config
import unittest


logging.config.fileConfig('logging.ini')
logger = logging.getLogger(__name__)


class NameOfTests(unittest.TestCase):
    def test_items_equal_dict_keys_and_list(self):
        di = dict(a=1, b=2)
        li = ['a', 'b']
        self.assertItemsEqual(di, li)


if __name__ == '__main__':
    unittest.main()
