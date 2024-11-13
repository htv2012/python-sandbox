import unittest
import ddt


test_data = {
    'int': 5,
    'bool': False,
    'str': '',
    'file_db': '/tmp/db',
}


partial_data = {k:v for k, v in test_data.items() if k == 'int'}


@ddt.ddt
class PartialDataTest(unittest.TestCase):
    @ddt.data(*(item for item in test_data if item == 'file_db'))
    def test_partial_method1(self, item):
        data = test_data[item]
        self.assertTrue(data)

    @ddt.data(*partial_data)
    def test_partial_method2(self, item):
        data = partial_data[item]
        self.assertTrue(data)

if __name__ == '__main__':
    unittest.main()
