# Example assumes this file is named test.py
# and lives in /home/nanodano/
# https://docs.python.org/3/library/os.path.html

import os

# Prints the full path of where the os.py module resides
print(os.__file__)


# The name of file where this print statement is written
print(__file__)
# test.py

# Get the full absolute path using os.path.abspath()
print(os.path.abspath(__file__))
# /home/nanodano/test.py

# Get the directory name of a file with os.path.dirname()
print(os.path.dirname(__file__))
# Relative to current directory
# Prints an empty string if being run from current directory
# Prints .. if being called from a deeper directory

# Combine to get absolute path of the directory containing the python file
print(os.path.abspath(os.path.dirname(__file__)))
# /home/nanodano

## Other functions that might be useful
# os.path.join()  # Join directory names using system specific dir separator
# os.sep()  # Path separator character (system specific)
# os.getcwd()  # Full absolute path
# os.walk()  # Generator to walk dirs recursively
# os.listdir()  # Current dir or specific dir