from sqlite3 import connect, Row

db = connect('test.db')  # Using the database created in previous example
db.row_factory = Row
cursor = db.cursor()

rows = cursor.execute('SELECT * FROM users')

print(type(rows))  # sqlite3.Cursor
for row in rows:
    print(type(row))  # sqlite3.Row
    print(row.keys())
    print(row)
    print(row['uSeRName'])