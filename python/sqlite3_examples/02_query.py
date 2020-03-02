from sqlite3 import connect

# Db setup
db = connect('test.db')
cursor = db.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, email TEXT)')
cursor.execute('INSERT INTO users (username, email) VALUES ("nanodano", "nanodano@devdungeon.com")')
db.commit()

# Query for rows and then iterate through results
rows = cursor.execute('SELECT * FROM users LIMIT 100')
print(type(rows))  # sqlite3.Cursor
for row in rows:
    print(type(row))  # tuple
    print(row)

# Query for rows and then use `fetchall()` to get as a list
rows = cursor.execute('SELECT * FROM users ORDER BY username ASC')
all_rows = rows.fetchall()  # Get a list of rows as tuples
print(all_rows)
# Or fetch a specific amount of rows
# some_rows.fetchmany(n)

# Db cleanup
cursor.close()
db.close()