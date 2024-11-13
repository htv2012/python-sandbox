#!/usr/bin/env python

list_1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
list_2 = [10,20,30]

list_1 = [row + [col] for row,col in zip(list_1, list_2)]
for row in list_1:
    print(row)
