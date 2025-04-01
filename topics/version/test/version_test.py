#!/usr/bin/env python
from hamcrest import (
    assert_that,
    equal_to,
    greater_than,
    greater_than_or_equal_to,
    less_than,
    less_than_or_equal_to,
)

from version import Version


def test_repr():
    assert_that(repr(Version("2.5.3")), equal_to("Version('2.5.3')"))


def test_str():
    assert_that(str(Version("4.5.67")), equal_to("4.5.67"))


def test_equal():
    assert_that(Version("3.5.7"), equal_to(Version("3.5.7")))


def test_equal_trailing_zero():
    assert_that(Version("3.5.7"), equal_to(Version("3.5.7.0")))


def test_less_than_with_same_length():
    assert_that(Version("3.5.7"), less_than(Version("3.5.8")))


def test_less_than_with_different_lengths():
    assert_that(Version("3.5.7"), less_than(Version("3.6")))


def test_less_than_with_zero():
    assert_that(Version("3.5"), less_than(Version("3.6.0")))


def test_less_than_or_equal():
    assert_that(Version("3.5.7"), less_than_or_equal_to(Version("3.5.7")))


def test_less_than_or_equal_when_less_than():
    assert_that(Version("3.5.7"), less_than_or_equal_to(Version("3.5.8")))


def test_less_than_or_equal_different_length():
    assert_that(Version("3.5.7"), less_than_or_equal_to(Version("3.6")))


def test_greater_than():
    assert_that(Version("3.5.8"), greater_than(Version("3.5.7")))


def test_greater_than_different_lengths1():
    assert_that(Version("3.6.0"), greater_than(Version("3.5")))


def test_greater_than_different_lengths2():
    assert_that(Version("3.6"), greater_than(Version("3.5.7")))


def test_greater_than_or_equal1():
    assert_that(Version("3.5.7"), greater_than_or_equal_to(Version("3.5.7")))


def test_greater_than_or_equal2():
    assert_that(Version("3.5.8"), greater_than_or_equal_to(Version("3.5.7")))


def test_greater_than_or_equal_different_lengths1():
    assert_that(Version("3.6"), greater_than_or_equal_to(Version("3.6.0")))


def test_greater_than_or_equal_different_lengths2():
    assert_that(Version("3.6.0"), greater_than_or_equal_to(Version("3.5")))
