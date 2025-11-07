import pytest

from gramlib import format_count


@pytest.mark.parametrize(
    "count, unit, expected",
    [
        (0, "monkey", "0 monkey"),
        (1, "bottle", "1 bottle"),
        (2, "batch", "2 batches"),
    ],
)
def test_format_count(count, unit, expected):
    assert format_count(count, unit) == expected
