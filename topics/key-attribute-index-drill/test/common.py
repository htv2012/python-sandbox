import types

import pytest


def tc(desc: str, **kwargs):
    """Create a pytest.param."""
    return pytest.param(
        types.SimpleNamespace(**kwargs),
        id=desc,
    )
