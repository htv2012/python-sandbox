from . import (
    normalize_coordinate,
)
from .board import Board


class TargetBoard(Board):
    _board_titlle = "TARGET"

    def mark(self, coord, result):
        coord = normalize_coordinate(coord)
        if coord not in self.grid:
            raise ValueError(f"Invalid coordinate: {coord}")
        self.grid[coord] = result
        self.shots_count += 1
