import csv
spreadsheet = csv.writer(open('data.csv', 'wb'), delimiter=',')
spreadsheet.writerow(["id", "username", "password"])
spreadsheet.writerow(["1", "admin", "admin"])
spreadsheet.writerow(["2", "ceo", "password1"])
