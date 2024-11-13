import pytest

from zig import Solution


@pytest.fixture
def convert():
    solution = Solution()
    return solution.convert


@pytest.mark.parametrize(
    "input_str,num_rows,expected",
    [
        pytest.param(
            "PAYPALISHIRING",
            3,
            "PAHNAPLSIIGYIR",
            id="example 1",
        ),
        pytest.param("PAYPALISHIRING", 4, "PINALSIGYAHRPI", id="example 2"),
        pytest.param("A", 1, "A", id="example 3"),
        pytest.param(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
            7,
            "AMYkwBLNXZjlvxCKOWaimuyDJPVbhntzEIQUcgosFHRTdfprGSeq",
            id="example 4",
        ),
        pytest.param(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            5,
            "AIQYBHJPRXZCGKOSWDFLNTVEMU",
            id="example 5",
        ),
    ],
)
def test_zigzag(input_str, num_rows, expected, convert):
    actual = convert(input_str, num_rows)
    assert actual == expected
