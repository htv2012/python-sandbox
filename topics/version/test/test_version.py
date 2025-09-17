#!/usr/bin/env python

from versionlib import Version


def test_repr():
    assert repr(Version("2.5.3")) == "Version('2.5.3')"


def test_str():
    assert str(Version("4.5.67")) == "4.5.67"


def test_equal():
    assert Version("3.5.7") == Version("3.5.7")


def test_equal_trailing_zero():
    assert Version("3.5.7") == Version("3.5.7.0")


def test_less_than_with_same_length():
    assert Version("3.5.7") < Version("3.5.8")


def test_less_than_with_different_lengths():
    assert Version("3.5.7") < Version("3.6")


def test_less_than_with_zero():
    assert Version("3.5") < Version("3.6.0")


def test_less_than_or_equal():
    assert Version("3.5.7") <= Version("3.5.7")


def test_less_than_or_equal_when_less_than():
    assert Version("3.5.7") <= Version("3.5.8")


def test_less_than_or_equal_different_length():
    assert Version("3.5.7") <= Version("3.6")


def test_greater_than():
    assert Version("3.5.8") > Version("3.5.7")


def test_greater_than_different_lengths1():
    assert Version("3.6.0") > Version("3.5")


def test_greater_than_different_lengths2():
    assert Version("3.6") > Version("3.5.7")


def test_greater_than_or_equal1():
    assert Version("3.5.7") >= Version("3.5.7")


def test_greater_than_or_equal2():
    assert Version("3.5.8") >= Version("3.5.7")


def test_greater_than_or_equal_different_lengths1():
    assert Version("3.6") >= Version("3.6.0")


def test_greater_than_or_equal_different_lengths2():
    assert Version("3.6.0") >= Version("3.5")
