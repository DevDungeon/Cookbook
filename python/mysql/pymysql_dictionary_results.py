from pymysql import connect
from pymysql.cursors import DictCursor

DB_HOST = 'example.net'  # IP or hostname of database
DB_NAME = 'asdf_test'  # Name of the database to use
DB_USER = 'asdf_test'  # Username for accessing database
DB_PASS = 'asdf'  # Password for database user

db_connection = connect(host=DB_HOST,
	                    user=DB_USER,
	                    password=DB_PASS,
	                    db=DB_NAME,
                        cursorclass=DictCursor)

with db_connection.cursor() as cursor:
    statement = "SELECT * FROM users"
    cursor.execute(statement)
    for row in cursor.fetchall():
        print(type(row))  # <class 'dict'>
        print(row)  # {'id': 9, 'username': 'nanodano', 'password': 'mysecret', 'email': 'nanodano@devdungeon.com'}
        print(row['id'])
        print(row['username'])
        print(row['email'])
db_connection.close()
