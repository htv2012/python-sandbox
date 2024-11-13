"""
In unittest, assertItemsEqual() does not work for lists of objects,
even if these objects implement the __eq__ method for comparison.

This module provide assertUnorderedListsEqual() which does the job.
"""
import unittest


def list_diff(a, b):
    """
    Return a - b
    Credit: Raymond Hettinger http://stackoverflow.com/a/7829388/459745
    """
    diff = list(a)
    for item in b:
        try:
            diff.remove(item)
        except ValueError:
            pass
    return diff


class User1(object):
    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def __repr__(self):
        return '{}({!r}, {!r})'.format(
            self.__class__.__name__,
            self.name, self.uid)

    def __eq__(self, other):
        return self.uid == other.uid and self.name == other.name


class ListOfItemsEqualTest(unittest.TestCase):
    def test_lists_that_are_equal(self):
        list1 = [User1('Bob', 501), User1('Alice', 502)]
        list2 = [User1('Alice', 502), User1('Bob', 501)]
        self.assertUnorderedListsEqual(list1, list2)

    def test_extra_in_first(self):
        list1 = [User1('Bob', 501), User1('Alice', 502), User1('Karen', 503)]
        list2 = [User1('Alice', 502), User1('Bob', 501)]
        self.assertUnorderedListsEqual(list1, list2)

    def test_extra_in_second(self):
        list1 = [User1('Alice', 502), User1('Bob', 501)]
        list2 = [User1('Bob', 501), User1('Alice', 502), User1('Bob', 501)]
        self.assertUnorderedListsEqual(list1, list2)

    def test_extra_in_both(self):
        list1 = [User1('Bob', 501), User1('Alice', 502), User1('Bob', 501)]
        list2 = [User1('John', 504), User1('Alice', 502), User1('Bob', 501)]
        self.assertUnorderedListsEqual(list1, list2, 'LIST ARE NOT THE SAME')

    def assertUnorderedListsEqual(self, list1, list2, error_prefix=''):
        """
        Compare two lists regardless of the items order

        :raise: AssertionError if they are not equal
        """
        only_in_first = list_diff(list1, list2)
        only_in_second = list_diff(list2, list1)
        if not only_in_first and not only_in_second:
            return

        error_message = error_prefix or 'Lists contain different items'
        if only_in_first:
            error_message += '\nItems that are only in first:\n- '
            error_message += '\n- '.join(str(x) for x in only_in_first)
        if only_in_second:
            error_message += '\nItems that are only in second:\n- '
            error_message += '\n- '.join(str(x) for x in only_in_second)
        self.fail(error_message)


if __name__ == '__main__':
    unittest.main()
