DATABASE_HOST = "example.com"
DATABASE_USER = ""
DATABASE_NAME = ""
DATABASE_PASSWD = ""
DATABASE_PORT = 3306

import MySQLdb

# Connect to db and create object
db = MySQLdb.connect(
	host=DATABASE_HOST,
	user=DATABASE_USER,
	passwd=DATABASE_PASSWD,
	db=DATABASE_NAME,
	port=int(DATABASE_PORT))

# Cursor we'll be using for commands
cursor = db.cursor()

# Get version single row query + fetch
cursor.execute("SELECT VERSION()")
version = cursor.fetchone()
print version

# Get all requests
numRows = cursor.execute("SELECT id, host_id, mime FROM requests")

for i in range(cursor.rowcount):
        row = cursor.fetchone()
        print row[0], row[1], row[2]	

""" # Printing rows example
rows = cursor.fetchall()
# Rows can be printed directly like rows[0][2]
for row in rows:
	for key, value in enumerate(row):
		print "Field #" + repr(key) + " - value: " + repr(value)
"""

""" # Insert example
#cursor.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
"""

""" # Another insert example
#sql = "INSERT INTO waves (sin, cos, tan, date) VALUES (%s, %s, %s, %s);"
#cursor.execute(sql % ( val1, val2, val3, s ))
"""