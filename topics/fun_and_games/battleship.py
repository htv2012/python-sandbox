#!/usr/bin/env python
import logging
import os


logging.basicConfig(level=os.getenv('LOGLEVEL', logging.WARN))
logger = logging.getLogger(__name__)


class Grid:
    HIT_MARKER = 100
    NO_SHIP_FOUND = object()
    START_ID = 1

    def __init__(self):
        self.ships = dict()
        self.health = dict()
        self.next_id = self.START_ID

    def assess(self, coordinate):
        """
        Assess the shot at coordinate.

        :param coordinate: The coordinate to assess
        :return: "hit", "miss", "sunk"
        """
        ship_id = self.ships.get(coordinate, self.NO_SHIP_FOUND)
        if ship_id == self.NO_SHIP_FOUND:
            return 'miss'

        if ship_id > self.HIT_MARKER:
            return 'was a hit'

        logger.debug('Ship ID: %r', ship_id)
        self.ships[coordinate] += self.HIT_MARKER
        self.health[ship_id] -= 1
        
        if self.health[ship_id] == 0:
            return 'sunk'

        return 'hit'

    def shoot(self, coordinate):
        """
        Shoot to a coordinate and print out the result
        """
        assessment = self.assess(coordinate)
        print('{} ==> {}'.format(coordinate, assessment))

    def add_ship(self, coordinates):
        """
        Add a ship to the grid

        :param coordinates: a sequence of coordinates which the ship
            occupies
        :return: the ship ID
        """
        for coordinate in coordinates:
            self.ships[coordinate] = self.next_id
        self.health[self.next_id] = len(coordinates)
        self.next_id += 1

    def __repr__(self):
        return 'Grid(ships={}, health={})'.format(self.ships, self.health)


if __name__ == '__main__':
    grid = Grid()
    grid.add_ship(('A1', 'A2', 'A3'))
    grid.add_ship(('D1', 'E1'))

    print(grid)
    grid.shoot('C9')
    grid.shoot('E1')
    grid.shoot('A3')
    grid.shoot('A2')
    grid.shoot('A1')
    grid.shoot('A1')
    print(grid)

