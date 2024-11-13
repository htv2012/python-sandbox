#!/usr/bin/env python3
gifts = [
    'a partridge in a pear tree', 'two turtle doves and', 'three French hens',
    'four calling birds', 'five gold rings', 'six geese a-laying',
    'seven swans a-swimming', 'eight maids a-milking', 'nine ladies dancing',
    'ten lords a-leaping', 'eleven pipers piping', 'twelve drummers drumming'
    ]
days = """first second third fourth fifth sixth seventh eighth
    ninth tenth eleventh twelfth""".split()
for limit, day in enumerate(days, 1):
    gift = '\n  '.join(reversed(gifts[:limit]))
    print(f'On the {day} day of Christmas, my true love gave to me\n  {gift}\n')
