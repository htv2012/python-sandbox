#!/usr/bin/env python3
"""
We have some complex setup and indenpendent assertions, a module-scope
fixture will do that. Furthermore, if we yield the fixture, we will
have exactly one set-up and one tear-down per module.

Notes

- Each test should not modify the return value of the fixture because
  it might affect the next test
- Tests are idependent from each other
- Tests should not rely on the order of execution
"""

import logging

import pytest


@pytest.fixture(scope="module")
def data():
    out = {"a": 1, "b": 2}
    logging.debug("Fixture data returns %r", out)
    yield out
    logging.debug("Clean up")


def test_a(data):
    assert data["a"] == 1


def test_b(data):
    assert data["b"] == 2
