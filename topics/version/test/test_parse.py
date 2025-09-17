#!/usr/bin/env python
from versionlib import parse_package


def test_no_version():
    assert parse_package("foo") == ("foo", "", "")


def test_equal():
    assert parse_package("foo==1.2.3") == ("foo", "==", "1.2.3")


def test_equal_with_spaces():
    assert parse_package("foo == 1.2.3") == ("foo", "==", "1.2.3")


def test_greater_than():
    assert parse_package("foo>1.2.3") == ("foo", ">", "1.2.3")


def test_greater_than_with_spaces():
    assert parse_package("foo > 1.2.3") == ("foo", ">", "1.2.3")


def test_greater_than_or_equal():
    assert parse_package("foo>=1.2.3") == ("foo", ">=", "1.2.3")


def test_greater_than_or_equal_with_spaces():
    assert parse_package("foo >= 1.2.3") == ("foo", ">=", "1.2.3")


def test_less_than():
    assert parse_package("foo<1.2.3") == ("foo", "<", "1.2.3")


def test_less_than_with_space():
    assert parse_package("foo < 1.2.3") == ("foo", "<", "1.2.3")


def test_less_than_or_equal():
    assert parse_package("foo<=1.2.3") == ("foo", "<=", "1.2.3")


def test_less_than_or_equal_with_spaces():
    assert parse_package("foo <= 1.2.3") == ("foo", "<=", "1.2.3")
