#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest
import os

from named_tuple_csv import NamedTupleReader


data_filename = os.path.join(os.path.dirname(__file__), 'users.csv')
assert os.path.exists(data_filename)


class NamedTupleReaderTest(unittest.TestCase):
    def setUp(self):
        self.data_file = open(data_filename)
        self.reader = NamedTupleReader(self.data_file)

    def test_header(self):
        self.assertEqual(('uid', 'alias', 'shell'), self.reader.fieldnames)

    def test_row(self):
        row = next(self.reader)
        self.assertEqual(('501', 'peter', 'bash'), row)
        self.assertEqual('501', row.uid)
        self.assertEqual('peter', row.alias)
        self.assertEqual('bash', row.shell)


if __name__ == '__main__':
    unittest.main()
