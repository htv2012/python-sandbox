#!/usr/bin/env python

import unittest
from ddt import ddt, data


class TestData(object):
    def __init__(self, name, container, sheet_visibility):
        self.name = name
        self.container = container
        self.sheet_visibility = sheet_visibility

    def __str__(self):
        return self.name


@ddt
class MyTest(unittest.TestCase):
    @data(TestData('edge_case', "story1", {"ws1": True, "ws2": False}),
          TestData('edge_fail', "story2", {"sw3": False}))
    def test1(self, tcdata):
        self.assertIn(tcdata.container, ["story", "story2"])


if __name__ == '__main__':
    unittest.main(verbosity=2)
