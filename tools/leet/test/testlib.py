import types

import pytest


def t(test_id: str, **kwargs):
    return pytest.param(types.SimpleNamespace(**kwargs), id=test_id)
