from itertools import accumulate
DAYS = "first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelveth".split()
VERSES = [
    "A partridge in a pear tree", "Two turtle doves, and", "Three french hens",
    "Four calling birds", "Five golden rings", "Six geese a-laying", "Seven swans a-swimming",
    "Eight maids a-milking", "Nine ladies dancing", "Ten lords a-leaping", "Eleven pipers piping",
    "Twelve drummers drumming"
]
for day, verse in zip(DAYS, accumulate(VERSES, lambda a, b: f"{b}\n{a}")):
    print(f"On the {day} day of Christmas, my true love sent to me")
    print(verse)
    print()
