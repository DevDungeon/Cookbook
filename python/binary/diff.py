# diff.py

import sys

file1 = open(sys.argv[1], 'rb')
data1 = file1.read()
file1.close()

file2 = open(sys.argv[2], 'rb')
data2 = file2.read()
file2.close()

if data1 != data2:
	print("Files do not match.")
else:
	print("Files match.")