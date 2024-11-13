"""Test the DFA."""
import pytest

from dfa import Machine


@pytest.fixture(scope="session")
def machine():
    m = Machine()
    m.add(0, {"a": 1})
    m.add(1, {"b": 2})
    m.add(2, {"c": 3})
    m.add(3, {}, is_end=True)
    return m


@pytest.mark.parametrize(
    "input_str,expected",
    [
        pytest.param("abc", True, id="happy path, whole"),
        pytest.param("xabcd", True, id="happy path, partial"),
        pytest.param("ab", False, id="not enough chars"),
    ],
)
def test_dfa(machine, input_str, expected):
    assert machine.solve(input_str) is expected
