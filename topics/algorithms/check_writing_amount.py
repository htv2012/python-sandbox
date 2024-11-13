#!/usr/bin/env python
"""
Convert number to check writting amount
"""
import collections
import math
import logging
import os


logging.basicConfig(level=os.getenv("LOGLEVEL", logging.WARN))
logger = logging.getLogger(__name__)


def plural(count, text):
    if count > 1:
        text += "s"
    return text


def check_writting_amount(amount):
    # Understands up to 99.99
    words_list = collections.deque()
    words = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "fourty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }

    amount = "{:<.2f}".format(amount)
    dollars, cents = [int(x) for x in amount.split(".")]
    logger.debug("After split, dollars={}, cents={}".format(dollars, cents))

    if cents != 0:
        words_list.append(plural(cents, "cent"))
        words_list.appendleft(str(cents))
        if dollars > 0:
            words_list.appendleft("and")

    logger.debug("words_list={}".format(words_list))
    return " ".join(words_list)

    dollar_word = "dollars" if dollars > 1 else "dollar"
    logger.debug("dollars=%d, cents=%d", dollars, cents)

    # Tens and ones
    if dollars < 10:
        words_list.append(words[dollars])
    elif 9 < dollars < 20:
        words_list.append(words[dollars])
    elif dollars >= 20:
        tens, ones = dollars // 10 * 10, dollars % 10
        logger.debug("tens={}, ones={}".format(tens, ones))
        words_list.append(words[tens])
        words_list.append(words[ones])

    # Cents
    words_list.append(dollar_word)
    if cents:
        words_list.extend(["and", "{}/100".format(cents)])

    words_list[0] = words_list[0].title()
    word_amount = " ".join(words_list)
    return word_amount


for amount in [
    0.75,
    15.9,
    3.5,
    2.0,
    79.83,
    12.93,
    48.75,
    99.99,
]:
    print("${:<8.2f} | {}".format(amount, check_writting_amount(amount)))
