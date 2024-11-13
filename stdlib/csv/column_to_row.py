import csv

header = ["uid", "alias", "shell", "is_admin"]
columns = dict(
    uid=[501, 502, 503],
    alias=["adam", "shelley", "jake"],
    shell=["bash", "tcsh", "default"],
    is_admin=[True, False, False],
)

with open("column_to_row.csv", "w") as f:
    writer = csv.writer(f, header)
    writer.writerow(header)
    writer.writerows(list(zip(*[columns[n] for n in header])))
