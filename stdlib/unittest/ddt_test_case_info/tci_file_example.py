import json
import unittest
import ddt
from atom.test_utilities.test_case_info import TestCaseInfo


def tci_from_file(json_filename):
    with open(json_filename) as f:
        json_data = json.load(f)
        test_cases = [TestCaseInfo(str(k), **v) for k, v in json_data.items()]
        return test_cases

@ddt.ddt
class MyTest(unittest.TestCase):
    @ddt.data(*tci_from_file('data.json'))
    def test1(self, tci):
        self.assertEqual(10, tci.foo)


if __name__ == '__main__':
    unittest.main()
