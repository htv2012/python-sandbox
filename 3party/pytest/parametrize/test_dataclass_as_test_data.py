#!/usr/bin/env python3
"""Idea: Use a dataclass for test case data."""
import dataclasses

import pytest


@dataclasses.dataclass
class TestData:
    """Describe test data.

    test_id:
        See the `id` parameter in pytest.param()
    port:
        A port number, must be > 1000
    """

    __test__ = False  # This is not a pytest test class

    test_id: str
    proto: str
    port: int

    @classmethod
    def make(cls, test_id, proto, port, marks=None):
        return pytest.param(
            cls(test_id, proto, port),
            id=test_id,
            marks=marks or [],
        )


@pytest.mark.parametrize(
    "test_data",
    [
        TestData.make(
            test_id="happy1",
            proto="http",
            port=3776,
        ),
        TestData.make(
            test_id="happy2",
            proto="https",
            port=4995,
        ),
    ],
)
def test1(test_data):
    assert test_data.proto in {"http", "https"}
    assert test_data.port > 1000
