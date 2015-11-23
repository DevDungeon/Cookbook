#binary_to_base64.py

# Binary to Base 64 (Tetrasexagesimal) and reverse
import sys
import base64

with open(sys.argv[1], 'rb') as file:
	binary_data = file.read()
	base64_string = base64.b64encode(binary_data)
	print(base64_string)