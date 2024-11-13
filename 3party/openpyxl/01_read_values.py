#!/usr/bin/env python3
"""
A Python skeleton script
"""
import openpyxl


def main():
    """ Entry """


if __name__ == "__main__":
    main()
    workbook = openpyxl.load_workbook("sample.xlsx")
    sheet = workbook.active
    print(sheet)

    for cell in ["A1", "B1", "C1", "D1"]:
        value = sheet[cell].value
        vtype = value.__class__.__name__
        # print(sheet[cell])
        print(f"{cell}: {value!r} ({vtype})")

