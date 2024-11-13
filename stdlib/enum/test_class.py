#!/usr/bin/env python
import enum

import pytest


class Color(enum.Enum):
    red = "#ff0000"
    green = "#00ff00"
    blue = "#0000ff"


def test_value():
    assert Color.red.value == "#ff0000"


def test_name():
    assert Color.green.name == "green"


def test_from_value():
    assert Color("#0000ff") == Color.blue


def test_from_value_failed():
    with pytest.raises(ValueError):
        Color("#000000")


def test_from_name():
    assert Color["red"] == Color.red


def test_from_name_failed():
    with pytest.raises(KeyError):
        Color["orange"]
