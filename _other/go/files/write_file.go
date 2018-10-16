package main

import (
	"os"
	"log"
)

func main() {
	// Open a new file for writing only
	// Truncate if it already has contents
	// Create if it does not exist
	file, err := os.OpenFile(
		"test.txt",
		os.O_WRONLY|os.O_TRUNC|os.O_CREATE,
		0666,
	)
	if err != nil {
		log.Fatal(err)
	}
	// File will close when function(main) returns
	defer file.Close()

	// Write bytes to file. You can easily write a string by casting
	// it to bytes like: []byte(myString)
	byteSlice := []byte("Bytes!\n")
	bytesWritten, err := file.Write(byteSlice)
	if err != nil {
		log.Fatal(err)
	}
	log.Printf("Wrote %d bytes.\n", bytesWritten)
}
