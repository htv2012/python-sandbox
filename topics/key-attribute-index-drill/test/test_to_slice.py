import pytest

from kai_drill import to_slice


@pytest.mark.parametrize(
    "token,expected",
    [
        pytest.param(":3", slice(None, 3), id="first N elements"),
        pytest.param("3:", slice(3, None), id="from Nth element on"),
        pytest.param("-3:", slice(-3, None), id="last N elements"),
        pytest.param("1:11", slice(1, 11), id="A to B"),
        pytest.param("10:0:-1", slice(10, 0, -1), id="reversed"),
    ],
)
def test_to_slice_expect_success(token, expected):
    assert to_slice(token) == expected


@pytest.mark.parametrize(
    "token,exception",
    [
        pytest.param("foo", ValueError, id="dict key"),
        pytest.param("12", ValueError, id="no colon"),
        pytest.param(":", ValueError, id="no digit"),
        pytest.param(":1:2:3", TypeError, id="too many colons"),
    ],
)
def test_to_slice_expected_raise(token, exception):
    with pytest.raises(exception):
        to_slice(token)
