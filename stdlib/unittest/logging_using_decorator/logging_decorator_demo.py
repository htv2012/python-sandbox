import unittest
import logtools


logger = logtools.create_logger(__name__, log_level=logtools.DEBUG)

@logtools.test_case_logger(logger)
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.value = 5

    def test1(self):
        logger.debug('Value: %d', self.value)
        self.assertEqual(self.value, 5)

    def test2(self):
        logger.debug('Make sure value %d is less than 10', self.value)
        self.assertLess(self.value, 10)


if __name__ == '__main__':
    unittest.main()
