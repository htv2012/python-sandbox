from random import choice
from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Static
from rich.style import Style
from rich.text import Text

# Colors to use (rich color names)
COLORS = ["red", "green", "blue", "black", "grey37", "purple", "yellow"]

BALL_CHAR = "●"  # solid circle

class Ball(Static):
    def __init__(self, color: str | None = None) -> None:
        super().__init__()
        self.color = color
        self.styles.padding = (0, 1)   # left/right spacing
        self.styles.margin = (0, 0)    # adjust if needed

    def render(self):
        if self.color:
            txt = Text(BALL_CHAR, style=Style(color=self.color))
        else:
            txt = Text(" ")  # empty space for empty column cells
        return txt

class ColumnsApp(App):
    CSS = """
Screen {
  align: center middle;
}

Grid {
  grid-size: 8 8;
  padding: 1;
}
Ball {
  padding-left: 1;
  padding-right: 1;
}

    """

    def compose(self) -> ComposeResult:
        grid = Grid()
        # Build column-major: 8 columns x 8 rows, but we want 7 columns filled, 1 empty column.
        # We'll place column by column; for Textual Grid with grid-size 8 8, adding widgets in order
        # fills row-major. To produce column-major appearance, we construct a 2D list and then add row-major.
        cols = []
        for col_index in range(8):
            column = []
            if col_index < 7:
                # fill with 8 random colored balls
                for _ in range(8):
                    color = choice(COLORS)
                    column.append(Ball(color))
            else:
                # empty column: use empty Ball (no color)
                for _ in range(8):
                    column.append(Ball(None))
            cols.append(column)

        # Convert column-major to row-major order for adding to the Grid
        for row in range(8):
            for col in range(8):
                grid.mount(cols[col][row])

        yield grid

if __name__ == "__main__":
    ColumnsApp().run()
