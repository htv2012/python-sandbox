import pytest
from common import context, tc

from kai_drill import to_slice


@pytest.mark.parametrize(
    "test_case",
    [
        # Happy-path cases
        tc(id="first N elements", token=":3", expected=slice(None, 3)),
        tc(id="from Nth element on", token="3:", expected=slice(3, None)),
        tc(id="last N elements", token="-3:", expected=slice(-3, None)),
        tc(id="A to B", token="1:11", expected=slice(1, 11)),
        tc(id="reversed", token="10:0:-1", expected=slice(10, 0, -1)),
        # Bad cases
        tc(id="bad: dict key", token="foo", exception=ValueError),
        tc(id="bad: no colon", token="12", exception=ValueError),
        tc(id="bad: no digit", token=":", exception=ValueError),
        tc(id="bad: too many colons", token=":1:2:3", exception=TypeError),
    ],
)
def test_to_slice(test_case):
    with context(test_case.exception):
        assert to_slice(test_case.token) == test_case.expected
