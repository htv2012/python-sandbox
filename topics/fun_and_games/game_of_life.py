#!/usr/bin/env python
from __future__ import print_function, unicode_literals
# whatis: given a 2D structure, find the neighbors of a cell


class Board:
    MAXROWS = 8
    MAXCOLS = 8
    EMPTY = None
    LIVE = "x"

    def __init__(self, coordinates=None):
        self.grid = {}
        for coordinate in coordinates or []:
            self.grid[coordinate] = Board.LIVE

    def print(self):
        """Print the board to the console"""
        print("   0 1 2 3 4 5 6 7")
        for row in range(Board.MAXROWS):
            print("%-2s " % row, end="")
            print(
                " ".join(self.grid.get((col, row), ".") for col in range(Board.MAXCOLS))
            )
        print()

    def update(self):
        """Update a gameboard based on the rules for game of life"""
        new_grid = {}
        for y in range(Board.MAXROWS):
            for x in range(Board.MAXCOLS):
                cell = self.grid.get((x, y))
                lives = self.count_lives(x, y)

                if cell == Board.LIVE and lives in {2, 3}:
                    new_grid[x, y] = Board.LIVE
                if cell == Board.EMPTY and lives == 3:
                    new_grid[x, y] = Board.LIVE

        self.grid = new_grid

    def count_lives(self, x, y):
        """Count the lives surrounding a coordinate"""
        count = 0
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),  # left
            (0, 1),  # bottom
            (1, 1),
            (1, 0),
            (1, -1),  # right
            (0, -1),  # top
        ]
        for dx, dy in directions:
            newx, newy = x + dx, y + dy
            if (
                0 <= newx < Board.MAXCOLS
                and 0 <= newy < Board.MAXROWS
                and self.grid.get((newx, newy)) == Board.LIVE
            ):
                count += 1

        return count


def main():
    """Game entry point"""
    board = Board([(3, 3), (4, 3), (5, 3), (2, 4), (3, 4), (4, 4)])
    board.print()
    board.update()
    board.print()
    board.update()
    board.print()


if __name__ == "__main__":
    main()
