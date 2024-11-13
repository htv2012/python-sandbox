# encoding: utf-8

"""
Use of file_data. A dictionary is recommended over a list because the
test name will be much nicer
"""

import unittest
from ddt import ddt, data, file_data

@ddt
class UserTest(unittest.TestCase):
    """ Example of using file_data """

    @file_data('dict.json')
    def test_shell(self, tcdata):
        uid, alias, shell = tcdata
        self.assertIn(shell, ["bash", "csh"])

    @file_data('list.json')
    def test_uid(self, tcdata):
        uid, alias, shell = tcdata
        self.assertGreater(uid, 500)


if __name__ == '__main__':
    unittest.main(verbosity=2)
