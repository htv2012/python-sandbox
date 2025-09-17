#!/usr/bin/env python

from versionlib import satisfied
from versionlib.version import _str2int


def test_equal():
    assert satisfied("3.1.5", "==", "3.1.5")
    assert satisfied("3.1", "==", "3.1")


def test_greater_than_or_equal():
    assert satisfied("3.1.5", ">=", "3.1.5")
    assert satisfied("3.1", ">=", "3.1")
    assert satisfied("3.1", ">=", "3.1.0")

    assert satisfied("3.1.5", ">=", "3.1.4")
    assert satisfied("3.2", ">=", "3.1")
    assert satisfied("3.1.1", ">=", "3.1")


def test_empty_requirement():
    assert satisfied("3.1.1", "", "")


def test_str2int_with_number():
    assert _str2int("9") == 9


def test_str2int_with_non_number():
    assert _str2int("foo") == "foo"


def test_str2int_with_mixed():
    assert _str2int("9a") == "9a"
