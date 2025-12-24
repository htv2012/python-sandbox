"""
For a dictionary, sort the keys from lowest value to highest
"""

import operator

# A list of grades, not in any order
grades = dict(John=95, Amanda=89, Jake=91, Betty=97)

print("Grades from highest to lowest:")
for student, grade in sorted(
    list(grades.items()), key=operator.itemgetter(1), reverse=True
):
    print("{0} {1}".format(grade, student))

print()
print("Students from A to Z:")
for student, grade in sorted(list(grades.items()), key=operator.itemgetter(0)):
    print("{0} {1}".format(grade, student))
