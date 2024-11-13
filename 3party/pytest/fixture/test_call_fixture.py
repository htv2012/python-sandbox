"""How do we call a fixture as a function.

We cannot call a fixture directly, but we can create a callable
function, then the fixture uses it.
"""

import pytest


def hello():
    return "hello"


@pytest.fixture
def hello_fixture():
    return hello()


def test_direct(hello_fixture):
    # Use fixture directly
    assert hello_fixture == "hello"


def test_indirect():
    # Cannot call a fixture, but can call function that make up the fixture
    assert hello() == "hello"
