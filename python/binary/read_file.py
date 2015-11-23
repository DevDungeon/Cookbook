import sys
import binascii

# Read the whole file at once. Large files limited by memory constraints
data = open(sys.argv[1], 'rb').read()
print(data)


# Read the file one chunk at a time. Good for large files
in_file = open(sys.argv[1], 'rb')
chunk_size = 1024 # Can be more than 1 byte
while True:
    bytes = in_file.read(chunk_size)
    if len(bytes) == 0:
        break
    yield bytes


# Read in chunks a different way
from functools import partial
chunk_size = 1024
with open(sys.argv[1], 'rb') as file:
	for byte in iter(partial(file.read, chunk_size), b''):
		print(byte)
		print(binascii.b2a_uu(byte))
		exit(0)