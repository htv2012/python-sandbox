#!/usr/bin/env python3
import pytest

from generate_parentheses import Solution


@pytest.fixture
def fut():
    """Function under test"""
    sol = Solution()
    return sol.generateParenthesis


@pytest.mark.parametrize(
    "n,expected",
    [
        pytest.param(
            3, ["((()))", "(()())", "(())()", "()(())", "()()()"], id="example 1"
        ),
        pytest.param(1, ["()"], id="example 2"),
        pytest.param(0, [], id="0"),
        pytest.param(1, ["()"], id="1"),
        pytest.param(
            4,
            [
                "(((())))",
                "((()()))",
                "((())())",
                "((()))()",
                "(()(()))",
                "(()()())",
                "(()())()",
                "(())(())",
                "(())()()",
                "()((()))",
                "()(()())",
                "()(())()",
                "()()(())",
                "()()()()",
            ],
            id="4",
        ),
    ],
)
def test_solution(fut, n, expected):
    actual = set(fut(n))
    expected = set(expected)
    missing = expected - actual
    extra = actual - expected
    assert actual == expected, f"\nMissing: {missing}\nExtra: {extra}"
