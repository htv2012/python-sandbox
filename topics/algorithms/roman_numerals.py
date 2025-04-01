#!/usr/bin/env python
"""Roman numerial examples"""

import re


def isValidRoman(roman):
    pat = """
        ^                                   # the start of the string
        M{0,3}                          # up to three thousands
        (CM|CD|D?C{0,3})            # the hundred
        (XC|XL|L?X{0,3})              # the tens
        (IX|IV|V?I{0,3})               # the ones
        $                                    # the end of the string
        """
    return None != re.search(pat, roman, re.VERBOSE)


def RomanToArabic(roman):
    "converts a valid roman number to arabic number"
    r = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    digits = " ".join(roman).split()  # list of digits
    digits.reverse()  # work from right to left
    arabic = 0
    lastD = "I"
    for d in digits:
        if r[d] < r[lastD]:
            arabic -= r[d]
        else:
            arabic += r[d]
        lastD = d
    return arabic


def ArabicToRoman(arabic):
    "converts from an arabic number to roman, asumming 1..1999"
    r = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    a = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ""
    for d in range(len(a)):
        while arabic >= a[d]:
            roman += r[d]
            arabic -= a[d]
    return roman


if __name__ == "__main__":
    print("2016 =", ArabicToRoman(2016))
    print(RomanToArabic(ArabicToRoman(1949)))
    for i in range(3999):
        if not isValidRoman(ArabicToRoman(i + 1)):
            print(i + 1, ArabicToRoman(i + 1))
