#!/usr/bin/env python3
"""
Use the -m smoke flag to select only those that are marked with
pytest.mark.smoke.
"""

import pytest


@pytest.mark.smoke
def test_1():
    assert True


@pytest.mark.smoke()
def test_2():
    assert True


def test_3():
    pass
