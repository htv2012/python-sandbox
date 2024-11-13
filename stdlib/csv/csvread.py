# whatis: csvread.py - demonstrates various classes for reading csv
import csv

datafile = "csvread.csv"

# ======================================================================
# Using the csv.reader class
# ======================================================================

print("Using the csv.reader class")
mycsv = csv.reader(open(datafile))
headers = next(mycsv)  # Read one line and return a list
print("%-16s %s" % (headers[0], headers[1]))

for line in mycsv:
    # We know in advance that our data file has 2 columns
    print("%-16s %s" % (line[0], line[1]))
print()

# ======================================================================
# Using the csv.DictReader class
# ======================================================================

print("Using the csv.DictReader class")
mycsv = csv.DictReader(open(datafile))
for line in mycsv:
    print(line)
    for field in mycsv.fieldnames:
        print("%-5s: %s" % (field, line[field]))
    print()
print()
