import pytest

from gramlib import plural


@pytest.mark.parametrize(
    "count, word, expected",
    [
        (1, "monkey", "1 monkey"),
        (2, "monkey", "2 monkeys"),
        (1, "bottle", "1 bottle"),
        (2, "batch(es)", "2 batches"),
        (3, "child|children", "3 children"),
    ],
)
def test_plural(count, word, expected):
    assert plural(count, word) == expected
