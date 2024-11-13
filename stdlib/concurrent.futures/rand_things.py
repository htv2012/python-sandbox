import random
import string

VOWELS = list("aeiouy")
CONSONANTS = [c for c in string.ascii_lowercase if c not in VOWELS]


def random_syllable():
    syllable = random.choice(CONSONANTS) + "".join(
        random.sample(VOWELS, random.randint(1, 3))
    )
    return syllable.title()


def random_word():
    return "".join(random_syllable() for _ in range(random.randint(1, 3)))


def random_title(words_count: int):
    title = " ".join(random_word() for _ in range(words_count))
    return title


