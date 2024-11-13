""" Use of class for generic test data """

import unittest
from ddt import ddt, data

class TestData(object):
    def __init__(self, name, **kwargs):
        self._name = name
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

    def __str__(self):
        """ Return the name so data driven works """
        return self._name

test_data = [
    TestData("pass_case", uid=501, alias="jakej", shell="bash"),
    TestData("fail_case", uid=502, alias="maggiej", shell="dash"),
]

@ddt        
class MyTest(unittest.TestCase):
    @data(*test_data)
    def test3(self, tcdata):
        self.assertIn(tcdata.shell, ["bash", "csh"])

if __name__ == '__main__':
    unittest.main()