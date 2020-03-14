import mysql
from mysql.connector import errorcode
from datetime import datetime

config = {
    'user': 'username',
    'password': 'password',
    'host': 'localhost',
    'database': 'database_name',
    'raise_on_warnings': True,
}

connection = None
try:
    connection = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exists")
    else:
        print(err)

cursor = connection.cursor()
data = ('test', 'username', 123, datetime.now())
add_message = ("INSERT INTO messages "
               " (message, username, thread_id, created) "
               " VALUES (%s, %s, %s, %s)")
cursor.execute(add_message, data)
inserted_id = cursor.lastrowid

connection.commit()

cursor.close()
connection.close()
