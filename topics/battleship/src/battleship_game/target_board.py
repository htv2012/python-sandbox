import io
from collections import defaultdict

from . import const


class TargetBoard:
    def __init__(self):
        self.grid = defaultdict(lambda: const.MARK_EMPTY)
        self.shots_count = 0

    def __str__(self):
        buf = io.StringIO()
        buf.write("TARGETS".ljust(const.BOARD_WIDTH))
        buf.write("\n\n")
        buf.write("  │ A │ B │ C │ D │ E │ F │ G │ H │ I │ J │\n")
        buf.write("──┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───│\n")

        for row in const.ROWS:
            buf.write(f"{row} │")
            for col in const.COLS:
                buf.write(f" {self.grid[col + row]} │")
            buf.write("\n")
            if row == "J":
                buf.write("──┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┘\n")
            else:
                buf.write("──┼───┼───┼───┼───┼───┼───┼───┼───┼───┼───│\n")

        shots_fired = f"{self.shots_count} shot(s) fired"
        buf.write(shots_fired.ljust(const.BOARD_WIDTH))
        buf.write("\n")

        return buf.getvalue()
