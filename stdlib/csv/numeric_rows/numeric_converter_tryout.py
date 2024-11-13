
import csv
from numeric_converter import row2numeric


# Try csv.reader
with open('data.csv') as f:
    reader = csv.reader(f)
    numeric_reader = map(row2numeric, reader)

    for row in numeric_reader:
        print(row)

# Try DictReader
print('---')
with open('data.csv') as f:
    reader = csv.DictReader(f)
    numeric_reader = map(row2numeric, reader)

    for row in numeric_reader:
        print(row)

