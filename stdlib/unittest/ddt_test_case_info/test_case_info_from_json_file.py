import unittest
import ddt
from atom.test_utilities.test_case_info import TestCaseInfo


# Add this to TestCaseInfo as a class method
def from_json(name, json_object):
    print 'json object:', json_object
    print 'items:', json_object.items()
    tci = TestCaseInfo(name, **json_object)
    return tci


@ddt.ddt
class MyTest(unittest.TestCase):
    @ddt.file_data('data.json')
    def test1(self, tc):
        tci = from_json('foo', tc)
        self.assertEqual(10, tci.foo)


if __name__ == '__main__':
    unittest.main()
