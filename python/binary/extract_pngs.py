# Extract PNGs from a file and put them in a pngs/ directory
import sys
with open(sys.argv[1], "rb") as binary_file:
    binary_file.seek(0, 2)  # Seek the end
    num_bytes = binary_file.tell()  # Get the file size

    count = 0
    for i in range(num_bytes):
        binary_file.seek(i)
        eight_bytes = binary_file.read(8)
        if eight_bytes == b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a":  # PNG signature
            count += 1
            print("Found PNG Signature #" + str(count) + " at " + str(i))
            png_size_bytes = binary_file.read(4)  # Next four bytes after signature is the IHDR with the length
            png_size = int.from_bytes(png_size_bytes, byteorder='little', signed=False)

            # Go back to beginning of image file and extract full thing
            binary_file.seek(i)
            png_data = binary_file.read(png_size + 8)  # The size of image plus the signature
            with open("pngs/" + str(i) + ".png", "wb") as outfile:
                outfile.write(png_data)
