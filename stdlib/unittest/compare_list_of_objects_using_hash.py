"""
In unittest, assertItemsEqual() does not work for lists of objects. A
closer examination of the sourcee shows that
"""
import unittest


class User(object):
    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def __repr__(self):
        return '{}({!r}, {!r})'.format(
            self.__class__.__name__,
            self.name, self.uid)

    def __hash__(self):
        """ Return a unique hash based on the attributes """
        model = (self.uid, self.name)
        return hash(model)

    def __eq__(self, other):
        return self.uid == other.uid and self.name == other.name


class ListOfItemsEqualTest(unittest.TestCase):
    def test_lists_that_are_equal(self):
        list1 = [User('Bob', 501), User('Alice', 502)]
        list2 = [User('Alice', 502), User('Bob', 501)]
        self.assertItemsEqual(list1, list2)

    def test_extra_in_first(self):
        list1 = [User('Bob', 501), User('Alice', 502), User('Karen', 503)]
        list2 = [User('Alice', 502), User('Bob', 501)]
        self.assertItemsEqual(list1, list2)

    def test_extra_in_second(self):
        list1 = [User('Alice', 502), User('Bob', 501)]
        list2 = [User('Bob', 501), User('Alice', 502), User('Bob', 501)]
        self.assertItemsEqual(list1, list2)

    def test_extra_in_both(self):
        list1 = [User('Bob', 501), User('Alice', 502), User('Bob', 501)]
        list2 = [User('John', 504), User('Alice', 502), User('Bob', 501)]
        self.assertItemsEqual(list1, list2, 'LIST ARE NOT THE SAME')


if __name__ == '__main__':
    unittest.main()
    print hash(User('bob', 501))
