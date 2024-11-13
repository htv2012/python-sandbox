#!/usr/bin/env python
# whatis: A simple hang-man game
import pathlib
import random


picture = [
r"""
|---|
|
|
|
|
=======
""",
r"""
|---|
|   O
|
|
|
=======
""",
r"""
|---|
|   O
|   |
|
|
=======
""",
r"""
|---|
|   O
|  /|
|
|
=======
""",
r"""
|---|
|   O
|  /|\
|
|
=======
""",
r"""
|---|
|   O
|  /|\
|  /
|
=======
""",
r"""
|---|
|   O
|  /|\
|  / \
|
=======
"""
]

THRESHOLD = len(picture) - 1


def get_random_word():
    words_file = pathlib.Path(__file__).with_name("hangman.words")
    with open(words_file) as f:
        words = f.read().split()
        random_word = random.choice(words)
        return random_word.upper()

class Player(object):
    def guess(self):
        letter = input('Guess: ').upper()
        return letter


class Hangman:
    def __init__(self, word):
        self.guesses = set()
        self._error_count = 0
        self.word = list(c.upper() for c in word)
        self.answer = list('_' for c in word)
        self.correct = set(self.word)

    def evaluate(self, letter):
        letter = letter.upper()

        if letter in self.correct:
            self.answer = [letter if letter == o else c for c, o in zip(self.answer, self.word)]
            is_correct = True
        else:
            if letter not in self.guesses:
                self._error_count += 1
            is_correct = False

        self.guesses.add(letter)
        return is_correct

    def show(self):
        print('\n\n{}'.format(picture[self.error_count]))
        print(' '.join(self.answer))
        print('Guesses so far: {}'.format(' '.join(sorted(self.guesses))))
        print('Errors: {}'.format(self.error_count))
        print()

    @property
    def error_count(self):
        return self._error_count

    @property
    def is_correct(self):
        return self.answer == self.word


    def __str__(self):
        return ' '.join(self.answer)

    def __repr__(self):
        return('Hangman(word={!r}, answer={!r}, guesses={!r}, errors={})'.format(
            ''.join(self.word), ''.join(self.answer), ''.join(sorted(self.guesses)), self.error_count))


def start_game(hangman, player):
    """
    Starts the game
    """
    error_count = 0
    guesses = set()
    over = False

    while not (hangman.is_correct or hangman.error_count == THRESHOLD):
        hangman.show()
        letter = player.guess()
        hangman.evaluate(letter)

    hangman.show()
    if hangman.is_correct:
        print('You won')
    else:
        print('You lost, the word is {}'.format(''.join(hangman.word)))


def main():
    """
    Entry point
    """
    hangman = Hangman(get_random_word())
    player = Player()
    start_game(hangman, player)


if __name__ == '__main__':
    main()
