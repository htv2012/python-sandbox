__author__ = 'hvu'

import unittest


class RetrospectionTest(unittest.TestCase):
    def setUp(self):
        self.testid = self.id()
        self.module_name, self.class_name, self.test_name = self.testid.split('.')

    def test_get_test_name(self):
        self.assertEqual('test_get_test_name', self.test_name)

    def test_get_class_name(self):
        self.assertEqual('RetrospectionTest', self.class_name)

    def test_get_module_name(self):
        self.assertEqual('retrospection_tests', self.module_name)

    def test_aimless(self):
        print self._testMethodName
        print self.__class__.__name__

class BaseClass(unittest.TestCase):
    def setUp(self):
        print 'In BaseClass.setUp(), self.id() ==>:', self.id()

class UseBaseTest(BaseClass):
    """ BaseClass.setUp() should give the correct class name, test name """
    def test1(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
