#!/usr/bin/env python
"""
Convert Excel workbooks to csv files
"""

import argparse
import csv
import pathlib

import openpyxl


def sheet2csv(sheet):
    def cell2str(cell):
        return "" if cell.value is None else str(cell.value)

    for row in sheet.iter_rows():
        fields = [cell2str(cell) for cell in row]
        if not any(fields):
            continue
        yield fields


def workbook2csv(workbook_path, output_dir):
    print(workbook_path)
    base_name = workbook_path.stem
    workbook = openpyxl.load_workbook(workbook_path)
    for worksheet in workbook.worksheets:
        rows = list(sheet2csv(worksheet))
        if not rows:
            continue
        csv_path = output_dir / f"{base_name}-{worksheet.title}.csv"
        print("-", csv_path)
        with open(csv_path, "w", encoding="utf-8") as csvf:
            writer = csv.writer(csvf)
            writer.writerows(rows)


def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-o",
        "--outdir",
        help="Directory to contain output CSV files",
        default=".",
        type=pathlib.Path,
    )
    parser.add_argument(
        "workbooks",
        help="The name of the input Excel workbook",
        nargs="+",
        type=pathlib.Path,
    )
    options = parser.parse_args()
    return options


def main():
    options = get_options()
    options.outdir.mkdir(exist_ok=True)
    for filename in options.workbooks:
        workbook2csv(filename, options.outdir)


if __name__ == "__main__":
    main()
