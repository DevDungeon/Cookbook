from openpyxl import Workbook
wb = Workbook()
ws = wb.active

ws['A1'] = "255.255.255.255"
ws.column_dimensions['A'].width = 15  # in characters, not pixels

wb.save('cell_resize_example.xlsx')
