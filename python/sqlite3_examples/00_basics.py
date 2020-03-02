"""
# Online docs:
https://docs.python.org/3/library/sqlite3.html

# Read docs locally
pydoc -p 9999
"""
from sqlite3 import connect

# Open or create a db from disk
db1 = connect('test.db')

# Open a memory-only db
db2 = connect(':memory:')

# Copy one db to another (backup)
# Can go from disk to disk, memory to disk, vice versa
db1.backup(db2)

db1.close()
db2.close()
