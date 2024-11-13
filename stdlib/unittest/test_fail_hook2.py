"""
Problem: I have some extra works to do when a test failed (like taking
    screenshot, or save off artifacts). How do I hook this into the
    unittest ecosystem?

Reference:
See solution by Alexander Petrovich from this page:
http://stackoverflow.com/a/15117842/459745

I like this solution better than the one on test_fail_hook.py
"""
import sys
import unittest
import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('test_fail_hook2')


class MyTest(unittest.TestCase):
    def test_expected_fail(self):
        self.assertEqual(2 + 2, 5)

    def test_expected_error(self):
        self.assertEqual(x, 5)

    def test_expected_pass(self):
        self.assertEqual(2, 2)

    def tearDown(self):
        test_name = self.id().split('.')[-1]
        exception_type, exception_value, _ = sys.exc_info()
        if exception_type is AssertionError:
<<<<<<< HEAD
            print ' --- failed in {}: {}'.format(test_name, exception_value)
        elif exception_type:
            print ' --- error in {}: {}'.format(test_name, exception_value)
=======
            logger.error('*** TEST FAILED: %s', exception_value)
        elif exception_type:
            logger.error('*** TEST ERROR:  %s', exception_value)
>>>>>>> 1396a7762b5b6db2f1eab93bec8546221d945fce


if __name__ == '__main__':
    unittest.main()
