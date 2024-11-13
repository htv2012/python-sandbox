import csv
import sys


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        reader = csv.DictReader(f)
        for row in reader:
            print row