#!/usr/bin/env python3
import pytest

from find_first import Solution


@pytest.fixture
def fut():
    """Function under test"""
    sol = Solution()
    return sol.strStr


@pytest.mark.parametrize(
    "haystack,needle,expected",
    [
        pytest.param("sadbutsad", "sad", 0, id="example 1"),
        pytest.param("leetcode", "leeto", -1, id="example 2"),
        pytest.param("xabcz", "abc", 1, id="middle match"),
        pytest.param("abc", "abc", 0, id="same string"),
        pytest.param("abc", "abcd", -1, id="needle is longer than haystack"),
    ],
)
def test_solution(fut, haystack, needle, expected):
    assert fut(haystack, needle) == expected
