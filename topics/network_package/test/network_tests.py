from network import (
    is_reachable,
    is_reachable_ssh,
    is_reachable_web,
    ping,
)

GOOGLE_HOST = "google.com"
NON_EXISTENT_HOST = "foobar.comx"


def test_is_reachable_positive():
    assert is_reachable(GOOGLE_HOST)


def test_is_reachable_negative():
    assert is_reachable(NON_EXISTENT_HOST) is False


def test_ping_is_analias_for_is_reachable():
    assert ping is is_reachable


def test_is_reachable_web_positive():
    assert is_reachable_web(GOOGLE_HOST)


def test_is_reachable_web_negative():
    assert is_reachable_web(NON_EXISTENT_HOST) is False


# Testing ssh port for positive is tricky, skip for now


def test_is_reachable_ssh_negative():
    assert is_reachable_ssh(NON_EXISTENT_HOST) is False
