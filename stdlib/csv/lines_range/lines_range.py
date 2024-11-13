#!/usr/bin/env python
"""
Parse a CSV file, only on certain lines
"""
import csv
import linecache


def get_lines(filename, start_line_number, end_line_number):
	"""
	Given a file name, start line and end line numbers,
	return those lines in the file
	"""
	for line_number in range(start_line_number, end_line_number + 1):
		yield linecache.getline(filename, line_number)


if __name__ == '__main__':
	# Get lines 4-6 inclusive in the file
	lines = get_lines('data.txt', 4, 6)
	reader = csv.reader(lines)

	for row in reader:
		print(row)
