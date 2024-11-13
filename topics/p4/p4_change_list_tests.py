import unittest
from p4_change_list import P4ChangeList


class P4ChangeListTest(unittest.TestCase):
    def test_cl_as_string(self):
        cl = P4ChangeList(561810)
        self.assertEqual('561810', cl.change_list)


if __name__ == '__main__':
    unittest.main()
