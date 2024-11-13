import unittest


class MyObject(object):
    def __init__(self):
        self.enabled = False


class MyTest(unittest.TestCase):
    def test_not_helpful(self):
        obj = MyObject()
        self.assertTrue(obj.enabled, 'Object is enabled')

if __name__ == '__main__':
    unittest.main()