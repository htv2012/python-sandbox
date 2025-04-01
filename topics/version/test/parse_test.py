#!/usr/bin/env python
from hamcrest import assert_that, equal_to

from version import parse_package


def test_no_version():
    assert_that(parse_package("foo"), equal_to(("foo", "", "")))


def test_equal():
    assert_that(parse_package("foo==1.2.3"), equal_to(("foo", "==", "1.2.3")))


def test_equal_with_spaces():
    assert_that(parse_package("foo == 1.2.3"), equal_to(("foo", "==", "1.2.3")))


def test_greater_than():
    assert_that(parse_package("foo>1.2.3"), equal_to(("foo", ">", "1.2.3")))


def test_greater_than_with_spaces():
    assert_that(parse_package("foo > 1.2.3"), equal_to(("foo", ">", "1.2.3")))


def test_greater_than_or_equal():
    assert_that(parse_package("foo>=1.2.3"), equal_to(("foo", ">=", "1.2.3")))


def test_greater_than_or_equal_with_spaces():
    assert_that(parse_package("foo >= 1.2.3"), equal_to(("foo", ">=", "1.2.3")))


def test_less_than():
    assert_that(parse_package("foo<1.2.3"), equal_to(("foo", "<", "1.2.3")))


def test_less_than_with_space():
    assert_that(parse_package("foo < 1.2.3"), equal_to(("foo", "<", "1.2.3")))


def test_less_than_or_equal():
    assert_that(parse_package("foo<=1.2.3"), equal_to(("foo", "<=", "1.2.3")))


def test_less_than_or_equal_with_spaces():
    assert_that(parse_package("foo <= 1.2.3"), equal_to(("foo", "<=", "1.2.3")))
