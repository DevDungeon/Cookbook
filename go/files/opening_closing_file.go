package main

import (
	"log"
	"os"
)

func main() {
	// Simple read only open
	file, err := os.Open("test.txt")
	if err != nil {
		log.Fatal(err)
	}
	file.Close()

	// Open for appending
	file, err = os.OpenFile("test.txt", os.O_APPEND, 0666)
	if err != nil {
		log.Fatal(err)
	}
	file.Close()

	// Various file modes for 3rd OpenFile parameter
	// Combine them with the or operator
	// e.g. os.O_CREATE|os.O_APPEND

	// os.O_RDONLY // Read only
	// os.O_WRONLY // Write only
	// os.O_RDWR // Read and write
	// os.O_APPEND // Append to end of file
	// os.O_CREATE // Create is none exist
	// os.O_TRUNC // Truncate file when opening
}
