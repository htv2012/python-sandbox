"""
Try to answer the question: if I don't have a setUp() or setUpClass(), will the base class'
counterparts get called?
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

class TestBase2(TestBase):
    def setUp(self):
        super(TestBase2, self).setUp()
        print 'TestBase2.setUp()'

class MyTestCase(TestBase2):
    def setUp(self):
        super(MyTestCase, self).setUp()
        print 'MyTestCase.setUp()'
    def test_something(self):
        print 'MyTestCase.test_something()'


if __name__ == '__main__':
    unittest.main()
