from battleship_game.game import Game


def f(coord):
    game.human.assess(coord)


game = Game()
game.start()
game.print()

while not game.game_over:
    game.human_fire()
    game.print()

if game.human.is_lost:
    print("You lose!")
else:
    print("You won!")
