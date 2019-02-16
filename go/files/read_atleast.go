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

	byteSlice := make([]byte, 512)
	minBytes := 8
	// io.ReadAtLeast() will return an error if it cannot
	// find at least minBytes to read. It will read as
	// many bytes as byteSlice can hold. 
	numBytesRead, err := io.ReadAtLeast(file, byteSlice, minBytes)
	if err != nil {
		log.Fatal(err)
	}
	log.Printf("Number of bytes read: %d\n", numBytesRead)
	log.Printf("Data read: %s\n", byteSlice)
}