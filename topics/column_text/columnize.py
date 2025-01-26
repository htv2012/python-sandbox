# import subprocess
import itertools
import shutil
import os
import logging

logging.basicConfig(level=os.getenv("LOGLEVEL", "WARNING"))


def columnize(elements: list[str], total_width: int = None):
    total_width = total_width or shutil.get_terminal_size().columns - 1
    max_width = max(len(e) for e in elements) + 2

    columns_count = total_width // max_width
    logging.debug("columns_count=%r", columns_count)

    rows_count = len(elements) // columns_count
    row_indices = list(range(rows_count))
    if columns_count * rows_count < len(elements):
        rows_count += 1

    rows = [[] for _ in row_indices]
    for element, row_index in zip(elements, itertools.cycle(row_indices)):
        rows[row_index].append(element)

    for row in rows:
        logging.debug("row=%r", row)
        for cell in row:
            print(cell.ljust(max_width), end="")
        print()
