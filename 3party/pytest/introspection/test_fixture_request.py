"""Show inside a request object."""

import logging

import pytest

import introspect


@pytest.fixture
def custom_fixture(request):
    logging.info("FROM A FIXTURE")
    logging.info(
        "Reference: https://docs.pytest.org/en/stable/reference/reference.html#std-fixture-request"
    )
    introspect.explore(request, "request")
    return None


def test_request(request, custom_fixture):
    logging.info("FROM A TEST")
    introspect.explore(request, "request")
    assert custom_fixture is None
