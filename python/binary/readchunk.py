#readchunk.py
import time
from functools import partial
import sys

image_path = sys.argv[1]

# Chunk size can be 
chunk_size = 50000000

with open(image_path, 'rb') as file:
	for byte in iter(partial(file.read, chunk_size), b''):
		#print(byte)
		time.sleep(4)
		exit(0)