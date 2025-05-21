from battleship_game.player import HumanPlayer

player = HumanPlayer()
player.add_ships()
b = player.ship_board
print(b)
print()
print(player.target_board)
