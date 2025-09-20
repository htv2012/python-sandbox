import pytest

from kai_drill import path_split


@pytest.mark.parametrize(
    "path,expected",
    [
        pytest.param("[0]", [(0, "index")], id="index"),
        pytest.param("[_key_1]", [("_key_1", "key")], id="key"),
        pytest.param("[tally total]", [("tally total", "key")], id="key with spaces"),
        pytest.param("[tally-total]", [("tally-total", "key")], id="key with dashes"),
        pytest.param(".attr", [("attr", "attribute")], id="attribute"),
        pytest.param("attr2", [("attr2", "attribute")], id="no leading dot"),
        pytest.param(
            "[_key_2].attr[0]",
            [("_key_2", "key"), ("attr", "attribute"), (0, "index")],
            id="combo",
        ),
    ],
)
def test_path_split(path, expected):
    assert path_split(path) == expected
