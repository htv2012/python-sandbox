import pathlib
import shutil
import unittest


class DbTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        original = pathlib.Path('short.db')
        if original.exists():
            original.rename('short.original')

    @classmethod
    def tearDownClass(cls):
        original = pathlib.Path('short.original')
        if original.exists():
            original.rename('short.db')

    def test1(self):
        pass


if __name__ == '__main__':
    unittest.main()
