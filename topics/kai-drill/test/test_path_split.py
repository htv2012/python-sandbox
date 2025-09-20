import pytest

from kai_drill import path_split


@pytest.mark.parametrize(
    "path,expected",
    [
        pytest.param(
            "[key1][_key_2].attr[0]",
            [("key1", "key"), ("_key_2", "key"), ("attr", "attribute"), (0, "index")],
            id="happy path",
        ),
    ],
)
def test_path_split(path, expected):
    assert path_split(path) == expected
