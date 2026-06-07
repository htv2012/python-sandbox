import collections
import random

from .asset import Asset
from .grid import Grid
from .stack import CAPACITY


def diag_grid() -> Grid:
    grid = Grid()
    balls = collections.deque(Asset.balls())
    for i in range(CAPACITY):
        for stack, ball in zip(grid[:-1], balls):
            stack.push(ball)
        balls.rotate(1)

    return grid


def horizontal_grid() -> Grid:
    grid = Grid()
    balls = Asset.balls()
    for stack in grid:
        for ball in balls:
            stack.push(ball)
    return grid


def random_grid() -> Grid:
    grid = Grid()
    balls = []
    for ball in Asset.balls():
        balls.extend([ball] * CAPACITY)

    random.shuffle(balls)
    for i, ball in enumerate(balls):
        stack_number = i // CAPACITY
        grid.put(stack_number, ball)

    return grid


def create_grid() -> Grid:
    grid_creators = [random_grid, horizontal_grid, diag_grid]
    grid_creator = random.choice(grid_creators)
    return grid_creator()
