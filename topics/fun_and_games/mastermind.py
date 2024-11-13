#!/usr/bin/env python
"""
A simple mastermind game
"""
import collections
import random


def show_banner():
    """
    Displays the game banner and instruction
    """
    print('\n\nM A S T E R M I N D')
    print('===================')
    print('I am thinking of a code of 4 digits, each digit is in the range')
    print('[1..6]. Make your guesses.')
    print()


def announce_won():
    """
    Announces that the player won
    """
    print('     You won!')


def announce_lost():
    """
    Announces that the player lost
    """
    print('     You lost!')


def show_feedback(digit_and_position, digit_only):
    """
    Displays the feedback to the player
    """
    print(f'     Correct digit and position: {digit_and_position}')
    print(f'     Correct digit, but not position: {digit_only}')
    print()


def show_code(code):
    """
    Displays the secret code
    """
    print(f'     The secret code is {code}')


def show_prompt(turn):
    """
    Displays a prompt to ask the player for a guess
    """
    print(f'{turn:>2} - Guess: ', end='')


def read_guess():
    """
    Reads the plaer's guess
    """
    return input()


def warn_incorrect_guess():
    """
    Informs the player of fowl move
    """
    print('     Please enter 4 digits, each in range 1..6')


def read_and_validate_guess(turn):
    """
    Read and validate user's input
    """
    while True:
        show_prompt(turn)
        guess = read_guess()

        if len(guess) != 4:
            warn_incorrect_guess()
            continue

        if not all('1' <= element <= '6' for element in guess):
            warn_incorrect_guess()
            continue

        return guess


def evaluate(secret, guess):
    """
    Evaluate the user's input against the secret code
    """
    # Count of those digits that are in the correct positions
    digit_and_position = sum(s == g for s, g in zip(secret, guess))

    secret_count = collections.Counter(secret)
    guess_count = collections.Counter(guess)

    # Count of those digits that are correct, but might or might not in
    # the correct position
    digit_only = sum(min(digit_count, secret_count.get(digit, 0))
                     for digit, digit_count in guess_count.items())
    digit_only -= digit_and_position

    return digit_and_position, digit_only


def main():
    """
    Entry
    """
    show_banner()
    secret = [random.randint(1, 6) for _ in range(4)]
    secret = ''.join(str(d) for d in secret)

    for turn in range(1, 11):
        guess = read_and_validate_guess(turn)
        digit_and_position, digit_only = evaluate(secret, guess)
        if digit_and_position == 4:
            announce_won()
            break
        show_feedback(digit_and_position, digit_only)
    else:
        announce_lost()

    show_code(secret)


if __name__ == '__main__':
    main()
