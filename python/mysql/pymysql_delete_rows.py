from pymysql import connect

DB_HOST = 'example.net'  # IP or hostname of database
DB_NAME = 'asdf_test'  # Name of the database to use
DB_USER = 'asdf_test'  # Username for accessing database
DB_PASS = 'asdf'  # Password for database user

db_connection = connect(host=DB_HOST,
	                    user=DB_USER,
	                    password=DB_PASS,
	                    db=DB_NAME)


with db_connection.cursor() as cursor:
    statement = """
        DELETE FROM users
        WHERE username=%s;
    """
    result = cursor.execute(statement, ('nanodano',))
    print(type(result))  # <class 'int'>
    print(result)  # Number of rows deleted

db_connection.commit()
db_connection.close()
