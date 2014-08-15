#encoding:utf-8
import xlrd
data = xlrd.open_workbook('d_excel.xls')
table = data.sheet_by_index(0)
row1 = table.row_values(0)
column1 = table.col_values(0)
cell = row1[0].encode('utf-8')
cell = column1[-1].encode('utf-8')
print row1, len(row1), type(row1)
print cell, len(cell), type(cell)
