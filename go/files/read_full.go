package main

import (
	"os"
	"log"
	"io"
)

func main() {
	// Open file for reading
	file, err := os.Open("test.txt")
	if err != nil {
		log.Fatal(err)
	}

	// io.ReadFull(file, byteSlice)
	// io func ReadFull(r Reader, buf []byte) (n int, err error)
	// The file.Read() function will happily read a 4 byte file in to
	// a 4096 byte slice. The io.ReadFull() function will return an
	// error if it the file does not have enough bytes to completely
	// fill up the slice.
	byteSlice := make([]byte, 2)
	numBytesRead, err := io.ReadFull(file, byteSlice)
	if err != nil {
		log.Fatal(err)
	}
	log.Printf("Number of bytes read: %d\n", numBytesRead)
	log.Printf("Data read: %s\n", byteSlice)
}