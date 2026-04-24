import contextlib
import types

import pytest


def context(exception):
    if exception is None:
        return contextlib.nullcontext()
    else:
        return pytest.raises(exception)


def tc(id: str, expected=None, exception=None, **kwargs):
    return pytest.param(
        types.SimpleNamespace(expected=expected, exception=exception, **kwargs),
        id=id,
    )
