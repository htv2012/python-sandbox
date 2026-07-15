#!/usr/bin/env python
import random


def jumble(w):
    """jumble/scramble a word"""
    li = " ".join(w).split()
    for i in range(len(li)):
        index1 = random.randint(0, len(li) - 1)
        index2 = random.randint(0, len(li) - 1)
        tempChar = li[index1]
        li[index1] = li[index2]
        li[index2] = tempChar
    jumbledWord = "".join(li)
    return jumbledWord


def main():
    # initialization
    wordList = [
        ["glasses", "can't read? wear these"],
        ["pigs", "three of them against the big bad wolf"],
        ["pencil", "mightier than a dagger"],
        ["excellent", "accept nothing less"],
        ["international", "the i in IBM"],
        ["scupture", "piece of art"],
    ]
    wordCount = len(wordList)
    USER_QUIT = "quit"
    USER_HINT = "hint"
    random.seed()  # initialize the random number generator

    # displays the program banner
    print()
    print("Welcome to Word Jumble")
    print("We scramble the words and you will guess them")
    print()

    # pick a random word
    r = random.randint(0, wordCount - 1)
    theWord = wordList[r][0]
    theHint = wordList[r][1]
    jumbleWord = jumble(theWord)
    # print "r = %d\nword = %s\nhint = %s\n" % (r, theWord, theHint)

    # init
    guess = ""
    score = 10
    while score > 0 and guess != USER_QUIT:
        print("\nJumbled word:", jumbleWord)
        print("Type 'hint', 'quit', or your guess")
        guess = input("> ")

        if guess == USER_HINT:
            score -= 5  # deduct for asking for a hint
            print("Hint:", theHint)  # display the hint
        elif guess == USER_QUIT:
            score = 0  # no point for loser
        elif guess == theWord:
            print("Congratulation. Your score is", score)
            break
        else:
            score -= 1
            print("Incorrect")

        if score == 0:
            print("Loser!")


if __name__ == "__main__":
    main()
