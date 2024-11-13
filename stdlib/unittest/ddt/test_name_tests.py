#!/usr/bin/env python

import unittest
from ddt import ddt, data, file_data

class TestData(object):
    def __init__(self, name, **kw):
        self.name = name
        for k, v in kw.items():
            setattr(self, k, v)
    def __str__(self):
        return self.name

test_data = [
    TestData('edge_case', uid=501, alias='alexm'),
    TestData('edge_fail', uid=500, alias='johnk'),
]



class TestCaseInfo(object):
    """ Class that holds test case name and test case data for ddt tests
    """
    def __init__(self, name, **kw):
        """ Constructor
            :param name: Test case name
            :param data: Test case data
        """
        if not isinstance(name, str) or not name:
            raise TypeError("name must be a non-empty string")
        self.__name__ = name

        for k,v in kw.items():
            setattr(self, k, v)

    # def __str__(self):
    #     """ Returns a string representation of the object
    #     """
    #     return self.name


tcdata2 = [
    TestCaseInfo('pass_case', uid=501, alias='cythiaw'),
    TestCaseInfo('fail_case', uid=500, alias='joant'),
]

print test_data
@ddt
class MyTest(unittest.TestCase):
    def test2(self):
        pass


    @data(*test_data)
    def test_user(self, tcdata):
        self.assertGreater(tcdata.uid, 500)

    @data(*tcdata2)
    def test_uid(self, tcdata):
        self.assertGreater(tcdata.uid, 500)

if __name__ == '__main__':
    unittest.main(verbosity=2)
