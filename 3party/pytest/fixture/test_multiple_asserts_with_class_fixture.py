#!/usr/bin/env python3
"""
Multiple independent asserts using class-scope fixture
"""

import logging

import pytest


@pytest.fixture(scope="class")
def test_data():
    """
    Create data for test.

    Using scope=class, this fixture is created once per class. That
    means each test should exercise care not to alter the fixture data,
    or subsequent tests might fail.
    """
    fixture_data = dict(a=1, b=2, c=3)
    logging.debug("data fixture created at memory location %r", id(fixture_data))
    return fixture_data


class TestItWithFailures:
    """Test with failures.

    The class in this case is just a grouping mechanism. The only
    shared data between tests is test_data.

    This class also demonstrates that modification of data will
    cause undesired effect. Furthermore, tests might be executed
    in any order, so please do not modify the test fixture.
    """

    def test_a_value(self, test_data):
        assert test_data["a"] == 1
        # Modify the data will cause test failure in subsequent tests
        test_data["b"] = 200
        test_data["c"] = 300

    def test_b_value(self, test_data):
        # Failed because of previous modification
        assert test_data["b"] == 2

    def test_c_value(self, test_data):
        # Failed because of previous modification
        assert test_data["c"] == 3


class TestWithSuccess:
    """Test with success.

    Because this class use a separate test_data from the previous
    class, its tests do not get affected.
    """

    def test_a_value(self, test_data):
        assert test_data["a"] == 1

    def test_b_value(self, test_data):
        assert test_data["b"] == 2

    def test_c_value(self, test_data):
        assert test_data["c"] == 3
