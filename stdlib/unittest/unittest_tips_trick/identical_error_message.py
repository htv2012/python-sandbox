import unittest

class MyTestCase(unittest.TestCase):
    def test_undo_redo(self):
        is_visisble = False

        self.assertTrue(is_visisble, 'Widget should be visible')

        # Simulate turning off visibility
        # is_visisble = not is_visisble

        # Simulate undo
        is_visisble = not is_visisble
        self.assertTrue(is_visisble, 'Widget should be visible')

if __name__ == '__main__':
    unittest.main()
