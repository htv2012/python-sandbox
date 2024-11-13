#!/usr/bin/env python3
import pytest

from length_of_last_word import Solution


@pytest.fixture
def fut():
    """Function under test"""
    sol = Solution()
    return sol.lengthOfLastWord


@pytest.mark.parametrize(
    "indata,expected",
    [
        pytest.param("Hello World", 5, id="example 1"),
        pytest.param("   fly me   to   the moon  ", 4, id="example 2"),
        pytest.param("luffy is still joyboy", 6, id="example 3"),
        pytest.param("", 0, id="empty string"),
        pytest.param("   ", 0, id="only spaces"),
        pytest.param("world  ", 5, id="trailing spaces"),
    ],
)
def test_solution(fut, indata, expected):
    assert fut(indata) == expected
