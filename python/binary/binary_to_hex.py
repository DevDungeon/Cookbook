#binary_to_hex.py
from functools import partial
import sys
import binascii

with open(sys.argv[1], 'rb') as file:
	for byte in iter(partial(file.read, 8), b''):
		# output = binascii.hexlify(byte
		print(byte)
		output = binascii.hexlify(byte)
		# sys.stdout.write(output)
		print(output)

print(binascii.unhexlify('FF00FF00'))

