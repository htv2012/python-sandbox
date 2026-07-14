import io

from . import const


class Board:
    _board_title = ""

    def __init__(self):
        self.grid = dict.fromkeys(const.ALL_COORDINATES, const.MARK_EMPTY)
        self.shots_count = 0

    @property
    def hits_count(self) -> int:
        hits = [
            mark
            for mark in self.grid.values()
            if mark in {const.MARK_HIT, const.MARK_SUNK}
        ]
        return len(hits)

    @property
    def sunks_count(self) -> int:
        hits = [mark for mark in self.grid.values() if mark == const.MARK_SUNK]
        return len(hits)

    def __str__(self):
        buf = io.StringIO()
        buf.write(self._board_title.ljust(const.BOARD_WIDTH))
        buf.write("\n\n")
        buf.write("  │ A │ B │ C │ D │ E │ F │ G │ H │ I │ J │\n")
        buf.write("──┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───│\n")

        for row in const.ROWS:
            buf.write(f"{row} │")
            for col in const.COLS:
                buf.write(f" {self.grid[row + col]} │")
            buf.write("\n")
            if row == const.ROWS[-1]:
                buf.write("──┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘\n")
            else:
                buf.write("──┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───│\n")

        status = f"Shots: {self.shots_count} | Hits: {self.hits_count} | Sunks: {self.sunks_count}"
        buf.write(status.ljust(const.BOARD_WIDTH))
        buf.write("\n")

        return buf.getvalue()
