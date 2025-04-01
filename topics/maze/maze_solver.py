#!/usr/bin/env python3
import logging
import os
import sys

logging.basicConfig(level=os.getenv("LOGLEVEL", logging.warn))
logger = logging.getLogger(__name__)


BLOCKED = 0
THROUGH = 1
VISITED = 2
TARGET = 9


def log_satus(status, row, col):
    logger.info("(%r, %r) %s", row, col, status)


def write_maze(file_handle, maze):
    file_handle.write("\n---\n")
    for row in maze:
        file_handle.write(" ".join(str(x) for x in row))
        file_handle.write("\n")
    file_handle.write("\n")


def print_maze(maze):
    write_maze(sys.stdout, maze)


def solve(maze, row, col):
    if maze[row][col] == TARGET:
        log_satus("target found", row, col)
        return True
    elif maze[row][col] == BLOCKED:
        log_satus("blocked", row, col)
        return False
    elif maze[row][col] == VISITED:
        log_satus("visited", row, col)
        return False

    # Gets here means the cell is not visited
    log_satus("visiting", row, col)
    maze[row][col] = VISITED

    # Go East
    if col + 1 < len(maze[0]) and solve(maze, row, col + 1):
        return True

    # Go North
    if row > 0 and solve(maze, row - 1, col):
        return True

    # Go West
    if col > 0 and solve(maze, row, col - 1):
        return True

    # Go South
    if row + 1 < len(maze) and solve(maze, row + 1, col):
        return True

    return False


if __name__ == "__main__":
    maze = [[1, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 9]]

    print_maze(maze)
    print(solve(maze, 0, 0))
    print_maze(maze)
