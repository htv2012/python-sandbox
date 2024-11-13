import operator
import types

import pytest


@pytest.fixture(
    params=[
        pytest.param(("add", 3, 5, 8), id="addition"),
        pytest.param(("mul", 3, 9, 27), id="multiplication"),
    ]
)
def data(request):
    op, left, right, expected = request.param
    op = getattr(operator, op)
    return types.SimpleNamespace(op=op, left=left, right=right, expected=expected)


def test_op(data):
    actual = data.op(data.left, data.right)
    assert actual == data.expected
