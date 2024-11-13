#!/usr/bin/env python
import xlwt

if __name__ == '__main__':
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet('My Sheet')
    sheet.write(0, 0, 'Hello')  # Row 1, col 1
    sheet.write(0, 1, 'World')  # Row 1, col 2
    workbook.save(__file__.replace('.py', '.xls'))
