import openpyxl
import excel2csv


def skip_first_n_rows(sheet, n):
    rows = excel2csv.sheet2csv(sheet)
    for _ in range(n):
        next(rows)
    return rows
    # for row in rows:
    #     yield row

if __name__ == '__main__':
    wb = openpyxl.load_workbook('example.xlsx')
    sh = wb.get_active_sheet()
    b1 = sh.cell('B1')
    a1 = sh.cell('A1')

    # Skip first n rows
    n = 0
    for row in skip_first_n_rows(sh, n):
        print(row)
