#read_bootsector.py
import sys

in_file = open(sys.argv[1], 'rb')
chunk_size = 512
data = in_file.read(chunk_size)
print(data)