import logging
import pathlib

import pytest

import sudoku

logger = logging.getLogger()


@pytest.fixture
def data_dir():
    here = pathlib.Path(__file__).parent
    return here / "data"


def test_solve(data_dir):
    puzzle = sudoku.load(data_dir / "original.ss")
    puzzle.mark_original()

    puzzle.solve()

    assert puzzle.original_intact
    assert puzzle.is_valid
