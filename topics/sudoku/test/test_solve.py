import logging

logger = logging.getLogger()


def test_solve(puzzle):
    puzzle.solve()

    assert puzzle.original_in_tact
    assert puzzle.is_valid
