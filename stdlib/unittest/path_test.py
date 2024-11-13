"""
Answer a few questions:

- Is __file__ the same as sys.argv[0]?
- Even when driven by nose or python -m unittest mymodule?

Try:

    python path_test.py  # passed
    python -m unittest path_test  # failed
    nosetests path_test.py  # failed
"""

import unittest
import sys


class MyTestCase(unittest.TestCase):
    def test_file_vs_sys_argv0(self):
        self.assertEqual(__file__, sys.argv[0])


if __name__ == '__main__':
    unittest.main()
