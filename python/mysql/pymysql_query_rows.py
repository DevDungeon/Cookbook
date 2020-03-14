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
    results = cursor.execute("SELECT * FROM users")
    print(type(results))  # <class 'int'>
    print(results)  # Number of rows selected

    # Extract data from the cursor
    single_row = cursor.fetchone()  # or `fetchall()`
    print(type(single_row))  # <class 'tuple'>
    print(single_row)  # Column data, e.g. (9, 'nanodano', 'mysecret', 'nanodano@devdungeon.com')

    # You can move the cursor back to the beginning (or a 'relative' position)
    # Moving it back to the beginning will let you iterate through the results again
    cursor.scroll(0, 'absolute')

    # You can also use `fetchall()` and iterate through list of tuples
    for row in cursor.fetchall():
        print(row)

    # Get the column names for the row tuples
    for column_details in cursor.description:
        print(column_details[0])  # Print column name
    
db_connection.close()
