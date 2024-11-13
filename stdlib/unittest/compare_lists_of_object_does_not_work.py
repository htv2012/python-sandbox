import unittest


class User(object):
    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def __repr__(self):
        return '{}({!r}, {!r})'.format(
            self.__class__.__name__,
            self.name, self.uid)


class ListOfItemsEqualTest(unittest.TestCase):
    def test_lists_that_are_equal(self):
        list1 = [User('Bob', 501), User('Alice', 502)]
        list2 = [User('Alice', 502), User('Bob', 501)]
        self.assertItemsEqual(list1, list2)


if __name__ == '__main__':
    unittest.main()
