from openpyxl import Workbook
wb = Workbook()
ws = wb.active

# Add some numbers
ws.append([27])
ws.append([13])
ws.append([35])

# Sum A1 to A3 and put it in B1
ws["B1"] = "=SUM(A1:A3)"

wb.save("formula.xlsx")