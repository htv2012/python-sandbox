#!/usr/bin/env python3
import pytest


@pytest.fixture
def config():
    """Returns the test's configurations"""
    return {
        "name": "foo",
        "port": 22,
    }


def test_use_fixture(config):
    assert config["name"] == "foo"
    assert config["port"] == 22
