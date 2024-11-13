import pytest


def test1():
    pass


@pytest.mark.require_env("TEST_SERVER_IP")
def test2():
    pass


@pytest.mark.require_env(
    "SERVER_IP", "This test depends on SERVER_IP environment variable"
)
def test3():
    pass
