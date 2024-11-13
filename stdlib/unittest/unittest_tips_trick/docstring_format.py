import unittest

class MyTestCase(unittest.TestCase):
    def test_that_failed(self):
        """
        Test 2 + 2, expect 4
        """
        self.assertEqual(2 + 2, 5)

if __name__ == '__main__':
    unittest.main()
