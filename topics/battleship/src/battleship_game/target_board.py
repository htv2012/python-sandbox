import io

from . import (
    ALL_COORDINATES,
    BOARD_WIDTH,
    COLS,
    MARK_EMPTY,
    MARK_HIT,
    MARK_SUNK,
    ROWS,
    normalize_coordinate,
)


class TargetBoard:
    def __init__(self):
        self.grid = dict.fromkeys(ALL_COORDINATES, MARK_EMPTY)
        self.shots_count = 0

    def mark(self, coord, result):
        coord = normalize_coordinate(coord)
        if coord not in self.grid:
            raise ValueError(f"Invalid coordinate: {coord}")
        self.grid[coord] = result
        self.shots_count += 1

    def __str__(self):
        buf = io.StringIO()
        buf.write("TARGETS".ljust(BOARD_WIDTH))
        buf.write("\n\n")
        buf.write("  │ A │ B │ C │ D │ E │ F │ G │ H │ I │ J │\n")
        buf.write("──┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───│\n")

        for row in ROWS:
            buf.write(f"{row} │")
            for col in COLS:
                buf.write(f" {self.grid[row + col]} │")
            buf.write("\n")
            if row == "J":
                buf.write("──┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘\n")
            else:
                buf.write("──┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───│\n")

        shots_fired = f"{self.shots_count} shot(s) fired"
        buf.write(shots_fired.ljust(BOARD_WIDTH))
        buf.write("\n")

        hits = [mark for mark in self.grid.values() if mark in {MARK_HIT, MARK_SUNK}]
        sunk_count = len([mark for mark in hits if mark == MARK_SUNK])
        damage = f"Hit count: {len(hits)}, sunk count: {sunk_count}"
        buf.write(damage.ljust(BOARD_WIDTH))
        buf.write("\n")

        return buf.getvalue()
