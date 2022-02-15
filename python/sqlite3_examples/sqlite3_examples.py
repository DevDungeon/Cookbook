# Online docs: https://docs.python.org/3/library/sqlite3.html
# Offline docs: pydoc -p 9999
import sqlite3

db = sqlite3.connect('test.db') # or ':memory:'

# Set this to get dict results instead of tuples
db.row_factory = Row 

## Backup to file or to another db object
db.backup('db.backup') 

## Get a db cursor
cursor = db.cursor()
statement = 'CREATE TABLE IF NOT EXISTS users (username TEXT, email TEXT)'
cursor.execute(statement)  # Returns None on create table
# CREATE TABLE statement does not require a commit, but others do

## Prepared statement (tuple + question marks)
statement = 'UPDATE users SET email=? WHERE username=?'
data = ('nanodano@devdungeon.com', 'nanodano')
cursor.execute(statement, data)
db.commit()

## Prepared statement (dict + named params)
statement = 'UPDATE users SET email=:email WHERE username=:username'
data = {
    'email': 'nanodano@devdungeon.com',
    'username': 'nanodano'
}
cursor.execute(statement, data)
db.commit()

## Execute many
row_data = [
  ('admin', 'admin@devdungeon.com'),
  ('nanodano', 'nanodano@devdungeon.com')
]
cursor.executemany("INSERT INTO users (username, email) VALUES (?, ?)", row_data)
db.commit()

## Inserting
cursor.execute('INSERT INTO users (username, email) VALUES ("nanodano", "nanodano@devdungeon.com")')
db.commit()
print(cursor.lastrowid) 

## Querying
rows = cursor.execute('SELECT * FROM users LIMIT 100')
# Either iterate through the rows
for row in rows:
    print(row)
# Or get the rows as a list
all_rows = rows.fetchall()
some_rows = rows.fetchmany(1)
one_row = rows.fetchone()

## Cleanup
db_cursor.close()
db.close()

## Error handling
# Refer to the exceptions: https://docs.python.org/3/library/sqlite3.html#exceptions