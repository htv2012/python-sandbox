#!/usr/bin/env python
"""
Find all paths through a maze
"""
import logging
import os


logging.basicConfig(level=os.getenv('LOGLEVEL', logging.WARN))
logger = logging.getLogger('all_routes')


THROUGH = '1'
BLOCKED = '0'
TARGET = '9'
VISITED = '2'
PATH = '3'


def load_maze(data):
    return [[c for c in r.strip().split(' ')] for r in data.strip().splitlines()]


def print_maze(maze):
    print('\n---')
    for row in maze:
        print(' '.join(row))


def all_routes(maze, route):
    row, column = route[-1]
    logger.debug('route=%r, row=%r, column=%r', route, row, column)
    visited = set(tuple(x) for x in route)
    logger.debug('visited=%r', visited)

    if maze[row][column] == TARGET:
        yield route
        return

    if maze[row][column] == BLOCKED:
        return

    # This is a through cell
    if row > 0 and (row - 1, column) not in visited:
        logger.debug('Go North')
        yield from all_routes(maze, route + [(row - 1, column)])

    if row + 1 < len(maze) and (row + 1, column) not in visited:
        yield from all_routes(maze, route + [(row + 1, column)])

    if column > 0 and (row, column - 1) not in visited:
        yield from all_routes(maze, route + [(row, column - 1)])

    if column + 1 < len(maze[0]) and (row, column + 1) not in visited:
        yield from all_routes(maze, route + [(row, column + 1)])


def shortest_route(maze, row, column):
    shortest = min((len(r), r) for r in all_routes(maze, [(row, column)]))
    return shortest


def main():
    maze = load_maze("""
        1 1 1 1
        1 0 9 1
        1 1 1 1
        0 1 1 1
        """)

    print_maze(maze)

    # All routes
    routes = all_routes(maze, [(0, 0)])
    print('---')
    for route in routes:
        print(route)

    # Shortest
    shortest = shortest_route(maze, 0, 0)
    print('---')
    print('Shortest: {} moves, path={}'.format(*shortest))


if __name__ == '__main__':
    main()
