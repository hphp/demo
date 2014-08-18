#encoding:utf-8

def for_excel_2007():
    #pip install openpyxl
    import openpyxl
    wb = openpyxl.load_workbook('d_excel.xlsx')
    # cant manipulate xls anymore.
    #sheet_names = wb.get_sheet_names()
    ws = wb.get_sheet_by_name("Sheet1")
    print ws.cell('A1').value
    # will just print the normal chinese instead of messy codes in spite of whether encoding:utf8 is set.

def for_excel_2003():
    import xlrd
    data = xlrd.open_workbook('d_excel.xls')
    table = data.sheet_by_index(0)
    row1 = table.row_values(0)
    column1 = table.col_values(0)
    cell = row1[0].encode('utf-8')
    cell = column1[-1].encode('utf-8')
    print row1, len(row1), type(row1)
    print cell, len(cell), type(cell)

for_excel_2007()
