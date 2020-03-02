from sqlite3 import connect


db = connect(':memory:')
cursor = db.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, email TEXT)')

cursor.execute('INSERT INTO users (username, email) VALUES ("admin", "admin@devdungeon.com")')
cursor.execute('INSERT INTO users (username, email) VALUES ("nanodano", "nanodano@devdungeon.com")')
print(cursor.lastrowid)  # Id of inserted row

rows = cursor.execute('SELECT * FROM users')
print('Users:')
for row in rows:
    print(row)

rows = cursor.execute('SELECT * FROM users')
# Get a list of rows as tuples
all_rows = rows.fetchall()  # Or rows.fetchmany(n)
for row in all_rows:
    print(row)
print(all_rows)
