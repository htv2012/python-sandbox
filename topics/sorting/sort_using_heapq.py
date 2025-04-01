#!/usr/bin/env python
"""
Use heapq to implement a list that is always sorted, find top N...
"""

import heapq

test_scores = [
    (95, "Jake M"),
    (87, "Danny B"),
    (99, "Alice W"),
    (88, "Amanda F"),
    (79, "John C"),
    (80, "Karen B"),
    (82, "Heather L"),
    (90, "Heather T"),
    (91, "Tom T"),
    (71, "Joe B"),
]

# Heap sort the test scores
heapq.heapify(test_scores)

# Top 3
print("Top three scores:")
for score in heapq.nlargest(3, test_scores):
    print("%3d - %s" % score)
