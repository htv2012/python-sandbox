import pathlib

import pytest

import sudoku


@pytest.fixture
def data_dir():
    here = pathlib.Path(__file__).parent
    return here / "data"


@pytest.fixture
def puzzle(data_dir):
    puz = sudoku.load(data_dir / "original.ss")
    return puz
