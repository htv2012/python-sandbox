import pytest

from pattern_matching import jump_table


@pytest.mark.parametrize(
    ["pattern", "in_char", "expected"],
    [
        pytest.param("banana", "b", 5, id="banana_b"),
        pytest.param("banana", "a", 6, id="banana_a"),
        pytest.param("banana", "n", 1, id="banana_n"),
        pytest.param("college", "c", 6, id="college_c"),
        pytest.param("college", "o", 5, id="college_o"),
        pytest.param("college", "l", 3, id="college_l"),
        pytest.param("college", "g", 1, id="college_g"),
        pytest.param("college", "e", 7, id="college_e"),
        pytest.param("college", "v", 7, id="college_not_found"),
    ],
)
def test_jump(pattern, in_char, expected):
    jump = jump_table(pattern)
    assert jump(in_char) == expected
