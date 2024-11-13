"""Test the get_home() function."""

import logging


def test_get_home(get_home):
    """Ensure that get_home() does not return None."""
    actual = get_home()
    logging.debug("get_home() returns %r", actual)
    assert get_home() is not None
