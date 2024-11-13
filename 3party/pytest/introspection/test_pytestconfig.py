"""Show inside a request object."""

import introspect


def test_pytestconfig(pytestconfig):
    introspect.explore(pytestconfig, "pytestconfig")
