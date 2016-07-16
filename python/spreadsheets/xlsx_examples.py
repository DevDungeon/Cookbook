from openpyxl import Workbook
wb = Workbook()
ws = wb.active  # Get active sheet (may not be the first one)

# Direct cell modification
ws['A1'] = "id"
ws['B1'] = "username"
ws['C1'] = "password"

# Add new row at bottom
ws.append(["1337", "NanoDano", "password1"])

# Can use Python datetime objects
import datetime
ws['D1'] = datetime.datetime.now()

wb.save("sample.xlsx")  # Write to disk
