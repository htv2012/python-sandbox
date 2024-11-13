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


class User2(object):
    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def __repr__(self):
        return '{}({!r}, {!r})'.format(
            self.__class__.__name__,
            self.name, self.uid)

def uid_equal(expected_user, actual_user, msg=None):
    if expected_user.uid != actual_user.uid:
        msg = '{} != {}. {}'.format(expected_user, actual_user, msg or '')
        raise AssertionError(msg)


class TypeEqualTest(unittest.TestCase):
    def setUp(self):
        self.addTypeEqualityFunc(User2, uid_equal)
        self.longMessage = True

    # def test_should_pass_user1(self):
    #     self.assertEqual(User1('Bob', 501), User1('Bob', 501))

    # def test_should_pass_user2(self):
    #     self.assertEqual(User2('Bob', 501), User2('Bob', 501))

    # def test_compare_using_eq(self):
    #     self.assertEqual(User1('Bob', 501), User1('Alice', 501))

    def test_compare_using_type_equality_registry(self):
        self.assertEqual(User2('Bob', 501), User2('Bob', 502), 'WHAT?')


if __name__ == '__main__':
    unittest.main(verbosity=2)
