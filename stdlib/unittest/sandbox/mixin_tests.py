"""
If a test class inherits from more than one class, only fixtures from
the first class take effect.
"""

import unittest

class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print 'TestBase.setUpClass()'
    @classmethod
    def tearDownClass(cls):
        print 'TestBase.tearDownClass()'
    def setUp(self):
        print 'TestBase.setUp()'
    def tearDown(self):
        print 'TestBase.tearDown()'


class MyMixin(unittest.TestCase):
    def setUp(self, workbook=None):
        """ This is not called: only the first setUp() count
        """
        print 'MyMixin.setUp(): workbook={}'.format(workbook)

    def helper1(self):
        print 'MyMixin.helper1()'

class UseMixin(TestBase, MyMixin):
    def test1(self):
        print 'UseMixin.test1()'
        self.helper1()


if __name__ == '__main__':
    unittest.main()
