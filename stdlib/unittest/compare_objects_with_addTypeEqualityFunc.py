"""
In unittest, when we need to compare two objects via assertEqual(), we
have two choices: implement the class' __eq__() or write a comparison
function and register it via addTypeEqualityFunc(). Each of these
approaches has its pros and cons.

The __eq__ Method
=================

Pros
----
* Clean and elegant: no need to register
* Reusable in other situation

Cons
----
* Sometimes, we don't have access to the class' source or allowed to
  change
* When assertEqual failed, if the object does not a __repr__ or __str__
  function, the output is not helpful
* Sometimes, we want to provide different ways to compare the two
  objects, but this method only provide one

The addTypeEqualityFunc Method
==============================

Pros
----
* Can Create different functions to compare the same object differently
* Can provide a helpful default error message

Cons
----
* Have to register via addTypeEqualityFunc
"""

import unittest


class User2(object):
    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def __repr__(self):
        return '{}(name={!r}, uid={!r})'.format(
            self.__class__.__name__, self.name, self.uid)


def create_comparison(exclude=tuple()):
    attrs = {'name', 'uid'} - set(exclude)
    def compare_function(u1, u2, msg=None):
        if msg is None:
            msg = 'Objects failed to compare'
        for attr in attrs:
            a1 = getattr(u1, attr)
            a2 = getattr(u2, attr)
            assert a1 == a2, msg + '. Attribute: {}'.format(attr)

    return compare_function


class TypeEqualTest(unittest.TestCase):
    def setUp(self):
        self.addTypeEqualityFunc(User2, create_comparison(exclude=['name']))
        self.longMessage = True

    def test_should_pass(self):
        self.assertEqual(User2('Karen', 501), User2('Bob', 501), 'Should pass')

    def test_should_fail(self):
        self.assertEqual(User2('Bob', 501), User2('Bob', 502))

    def test_list_of_objects(self):
        list1 = [User2('Bob', 501), User2('Ann', 502)]
        list2 = [User2('Amy', 501), User2('Ian', 502)]
        for u1, u2 in zip(list1, list2):
            self.assertEqual(u1, u2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
