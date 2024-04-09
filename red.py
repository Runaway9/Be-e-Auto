import openpyxl
excel = openpyxl.load_workbook('C:/bee/beedata.xlsx')
sheet = excel.get_sheet_by_name('beedata')
cell = sheet['A1']
print(cell.value)