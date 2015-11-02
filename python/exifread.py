import exifread
import sys

with open(sys.argv[1], 'rb') as file:
	tags = exifread.process_file(file)
	for tag in tags:
		print(tag)
		print(tags[tag])
