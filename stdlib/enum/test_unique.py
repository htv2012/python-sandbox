#!/usr/bin/env python
import enum

import pytest


def test_uniqueness_violation():
    with pytest.raises(ValueError, match="duplicate values found"):

        @enum.unique
        class Color(enum.Enum):
            red = 1
            yellow = 2
            amber = 2
