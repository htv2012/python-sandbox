import collections
from io import StringIO


EMPTY = '.'
ROWS = 9
COLS = 9


class Board(collections.Sequence ):
    def __init__(self):
        self.grid = [[EMPTY for c in range(COLS)]
            for r in range(ROWS)]

    def __getitem__(self, index):
        return self.grid[index]

    def __len__(self):
        return len(self.grid)

    def __str__(self):
        # return '\n'.join(' '.join(c for c in row) for row in self)
        buf = StringIO()
        for row, cells in enumerate(self.grid):
            for col, cell in enumerate(cells):
                buf.write('%s ' % cell)
                if col == 2 or col == 5:
                    buf.write('| ')
            buf.write('\n')
            if row == 2 or row == 5:
                buf.write('------+-------+-------\n')
        return buf.getvalue()

    def read(self, text_rows):
        self.grid = [row.split() for row in text_rows]

    def candidates(self, row, col):
        all_candidates = set('123456789')
        if self[row][col] in all_candidates:
            return []

        # Case: for empty cell
