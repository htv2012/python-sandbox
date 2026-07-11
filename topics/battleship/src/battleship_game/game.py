import itertools

from .player import ComputerPlayer, HumanPlayer


class Game:
    def __init__(self):
        self.players = [HumanPlayer(), ComputerPlayer()]

    def start(self):
        for player in self.players:
            player.add_ships()
        self.print()

        turns = itertools.cycle([(0, 1), (1, 0)])
        while not self.game_over:
            sending, receiving = next(turns)
            sender = self.players[sending]
            receiver = self.players[receiving]

            coord = sender.move()
            result = receiver.assess(coord)
            sender.mark(coord, result)
            self.print()

        if self.players[0].is_lost:
            print("You lost")
        else:
            print("You won")

    @property
    def game_over(self) -> bool:
        """When one of the player wins."""
        return any(player.is_lost for player in self.players)

    def print(self):
        """Show human ship- and target boards."""
        human = self.players[0]
        sb = str(human.ship_board).splitlines()
        tb = str(human.target_board).splitlines()
        sep = " " * 8
        for line in zip(sb, tb):
            print(sep.join(line))


def main():
    game = Game()
    game.start()
