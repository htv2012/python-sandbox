import csv


def transform_row(input_row):
    output_row = input_row[:]
    output_row[10:12] = [' '.join(output_row[10:12])]
    return output_row

if __name__ == '__main__':
    with open('data.csv') as inf, open('out.csv', 'wb') as outf:
        reader = csv.reader(inf)
        writer = csv.writer(outf)
        writer.writerows(transform_row(row) for row in reader)
