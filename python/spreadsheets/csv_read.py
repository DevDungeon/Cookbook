import csv
filename = 'data.csv'
spreadsheet = csv.reader(open(filename, 'rb'), delimiter=',')
for row in spreadsheet:
    print(row)  # List of columns
    # Access individual columns with index like row[0]