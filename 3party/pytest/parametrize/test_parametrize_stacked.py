#!/usr/bin/env python3
import pytest


@pytest.mark.parametrize("second", ["abc", "def"])
@pytest.mark.parametrize("first", [1, 2, 3])
def test_add(first, second):
    pass
