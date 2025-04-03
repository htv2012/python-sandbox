import pytest

from pattern_matching import match


@pytest.mark.parametrize(
    ["haystack", "needle", "expected"],
    [
        pytest.param("abcdef", "def", 3, id="happy_path1"),
        pytest.param("aefdef", "def", 3, id="happy_path2"),
        pytest.param("welcome to colorado", "color", 11, id="happy_path3"),
        pytest.param("abcd", "abcd", 0, id="exact_match"),
    ],
)
def test_match(haystack, needle, expected):
    assert match(haystack, needle) == expected


@pytest.mark.parametrize(
    ["haystack", "needle"],
    [
        pytest.param("abc", "kbc", id="not_found"),
        pytest.param("abcdef", "", id="empty_pattern"),
        pytest.param("hay", "needle", id="short_haystack"),
        pytest.param("noodle", "needle", id="same_length"),
    ],
)
def test_not_match(haystack, needle):
    with pytest.raises(ValueError):
        match(haystack, needle)
