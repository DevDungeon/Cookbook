from openpyxl import Workbook
wb = Workbook()
ws = wb.active

ws['A1'] = "255.255.255.255"
ws.column_dimensions['A'].width = 15  # In characters, not pixels
ws.row_dimensions[1].height = 400  # In pixels

wb.save('cell_resize_example.xlsx')
