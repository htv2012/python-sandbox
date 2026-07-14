import pytest

from battleship_game.player import is_consecutive


@pytest.mark.parametrize(
    ["ship", "expected"],
    [
        pytest.param(["a1", "b1", "c1"], True, id="happy path"),
        pytest.param(["a1", "b1", "d1"], False, id="non consecutive column"),
        pytest.param(["a1", "a2", "a4"], False, id="non consecutive row"),
    ],
)
def test_is_consecutive(ship, expected):
    assert is_consecutive(ship) is expected
