package main

import (
	"os"
	"log"
)


func main() {
	// Open file for reading
	file, err := os.Open("test.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	// Read up to len(b) bytes from the File.
	// Zero bytes written means end of file
	// EOF returns error type io.EOF
	// func (f *File) Read(b []byte) (n int, err error)
	byteSlice := make([]byte, 16)
	numBytesRead, err := file.Read(byteSlice)
	if err != nil {
		log.Fatal(err)
	}
	log.Printf("Number of bytes read: %d\n", numBytesRead)
	log.Printf("Data read: %s\n", byteSlice)

	// If the byte slice was too small and whole file
	// was not read, the pointer will be mid file.
	// Use Seek() to figure out where you are currently
	// in the file. You might have to perform several
	// reads if you have a small buffer to get the whole file.
	position, err := file.Seek(0, 1)
	if err != nil {
		log.Fatal(err)
	}
	log.Printf("At position: %d\n", position)	
}