"""
Starts with a bunch of coins, two players take turn to remove 1, 2, or 3
coins from the bunch. The winner is the one who remove the last coin(s).
"""

import random
import itertools


def human_turn(number_of_coins):
    taken = int(input("How many: ".format(number_of_coins)))
    return taken


def computer_turn(number_of_coins):
    taken = (number_of_coins % 4) or random.randint(1, 3)
    print("Computer takes {}".format(taken))
    return taken


print("Welcome to a game of Nim")
coin_count = int(input("How many coins to start with? "))
print()

for player, turn in itertools.cycle([("You", human_turn), ("Computer", computer_turn)]):
    taken = turn(coin_count)
    coin_count -= taken

    print(coin_count, "coin(s) left")

    if coin_count == 0:
        print()
        print(player, "won")
        break

    print()
