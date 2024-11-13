from collections import Mapping
import unittest
import ddt


class TestCaseInfo(Mapping):
    """ Class that holds test case data for DDT tests """

    def __init__(self, name, data, **kwargs):
        if not isinstance(name, basestring) or not name:
            raise TypeError("Name must be a non-empty string")
        self.name = name
        self.data = data
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.__dict__)

    def __iter__(self):
        return iter({k: v for k, v in self.__dict__.iteritems() if k not in {'name', 'data'}})

    def __getitem__(self, key):
        return getattr(self, key)


test_cases = [
    TestCaseInfo('foo', 'foo test', x=1, y=2),
    TestCaseInfo('bar', 'bar test', x=3, y=4),
]


@ddt.ddt
class MyTest(unittest.TestCase):
    @ddt.unpack
    @ddt.data(*test_cases)
    def test1(self, x, y):
        print('x = {}, y = {}'.format(x, y))
        self.assertIsNone(x)


if __name__ == '__main__':
    unittest.main()
