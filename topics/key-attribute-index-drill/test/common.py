import contextlib

import pytest


def context(exception):
    if exception is None:
        return contextlib.nullcontext()
    else:
        return pytest.raises(exception)
