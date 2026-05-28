import io

from .stack import EMPTY_VALUE


def draw_grid(grid):
    buf = io.StringIO()
    buf.write("\n")
    buf.write("│ ")
    buf.write(" │ ".join("✅" if stack.is_completed else "◼️" for stack in grid))
    buf.write(" │\n")
    buf.write("│ 0️⃣ │ 1️⃣ │ 2️⃣ │ 3️⃣ │ 4️⃣ │ 5️⃣ │ 6️⃣ │ 7️⃣ │\n")
    for row in zip(*[stack.as_column for stack in grid]):
        buf.write("│ ")
        buf.write(" │ ".join("◼️" if c == EMPTY_VALUE else c for c in row))
        buf.write(" │\n")

    print(buf.getvalue())
