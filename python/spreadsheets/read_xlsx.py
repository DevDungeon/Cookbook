from openpyxl import load_workbook

wb = load_workbook(filename='users.xlsx')

# List sheets available
sheets = wb.get_sheet_names()
print(sheets)

# Load active sheet or named sheet
sheet = wb.active
# sheet = wb['User Information']

print(sheet['A1'].value)  # Read a specific cell