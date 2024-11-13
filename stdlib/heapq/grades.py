#!/usr/bin/env python3
from __future__ import print_function

import heapq
from collections import namedtuple


def print_grades(label, grade_list):
    print("#", label)
    for grade in grade_list:
        print(grade)
    print()


Grade = namedtuple("Grade", ["score", "name"])

grades = [
    Grade(83, "John"),
    Grade(84, "Karen"),
    Grade(91, "Anna"),
    Grade(79, "Josh"),
    Grade(77, "Padma"),
]

print_grades("Original Grades", grades)

heapq.heapify(grades)
print_grades("Heapified Grades", grades)

heapq.heappush(grades, Grade(85, "Kim"))
print_grades("Grades after adding Kim", grades)
