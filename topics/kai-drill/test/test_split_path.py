import pytest

from kai_drill import TokenKind, split_path


@pytest.mark.parametrize(
    "path,expected",
    [
        pytest.param("[0]", [(0, TokenKind.KEY_OR_INDEX)], id="index"),
        pytest.param("[:3]", [(slice(None, 3), TokenKind.KEY_OR_INDEX)], id="slice1"),
        pytest.param("[_key_1]", [("_key_1", TokenKind.KEY_OR_INDEX)], id="key"),
        pytest.param(
            "[tally total]",
            [("tally total", TokenKind.KEY_OR_INDEX)],
            id="key with spaces",
        ),
        pytest.param(
            "[tally-total]",
            [("tally-total", TokenKind.KEY_OR_INDEX)],
            id="key with dashes",
        ),
        pytest.param(".attr", [("attr", TokenKind.ATTRIBUTE)], id="attribute"),
        pytest.param("attr2", [("attr2", TokenKind.ATTRIBUTE)], id="no leading dot"),
        pytest.param(
            "[_key_2].attr[0]",
            [
                ("_key_2", TokenKind.KEY_OR_INDEX),
                ("attr", TokenKind.ATTRIBUTE),
                (0, TokenKind.KEY_OR_INDEX),
            ],
            id="combo",
        ),
    ],
)
def test_path_split(path, expected):
    assert split_path(path) == expected
