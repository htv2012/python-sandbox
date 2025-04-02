class Player:
    def __init__(self, name: str = None):
        self.name = name

    def move(self):
        raise NotImplementedError()

    def add(self):
        raise NotImplementedError()


class HumanPlayer(Player):
    def move(self):
        pass

    def add(self):
        return [input("Enter ship coordinates: ").split() for _ in range(5)]
