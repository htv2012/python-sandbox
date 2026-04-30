"""Plays rock, paper, scissors against a bot."""

import collections
import enum
import pathlib
import random

USER_PHRASES = [
    "You beats the smartest bot in the universe!",
    "Congratulations!",
    "You won. Did you cheat?",
]

BOT_PHRASES = [
    "Is that all you can do?",
    "You cannot defeat the smartest bot in the universe.",
    "I can read your mind.",
]


class Move(enum.StrEnum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"

    def __gt__(self, other):
        return (
            (self == Move.ROCK and other == Move.SCISSORS)
            or (self == Move.PAPER and other == Move.ROCK)
            or (self == Move.SCISSORS and other == Move.PAPER)
        )


def make_user_choice():
    table = {"r": "rock", "p": "paper", "s": "scissors"}
    while (user_input := input("[r]ock, [p]aper, or [s]cissors: ")) not in "rps":
        print("that is not a valid imput. Please try again")
    return Move(table[user_input])


def make_computer_choice():
    return random.choice(list(Move))


def main():
    print(pathlib.Path("README.md").read_text())
    scores = collections.Counter()
    while not (scores["user"] == 3 or scores["bot"] == 3):
        user_choice = make_user_choice()
        bot_choice = make_computer_choice()

        print(f"User: {user_choice}, bot: {bot_choice} => ", end="")

        if user_choice > bot_choice:
            scores["user"] += 1
            print("user wins")
        elif bot_choice > user_choice:
            scores["bot"] += 1
            print("bot wins ")
        else:
            print("tie      ")

        print(f"Score (user:bot): {scores['user']}:{scores['bot']}")
        print()

    if scores["user"] == 3:
        phrase = random.choice(USER_PHRASES)
    else:
        phrase = random.choice(BOT_PHRASES)
    print(phrase)


if __name__ == "__main__":
    main()
