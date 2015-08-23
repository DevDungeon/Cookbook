package main

import (
	"os"
	"log"
	"io"
)

// Copy a file
func main() {
	// Open original file
	originalFile, err := os.Open("test.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer originalFile.Close()

    // Create new file
    newFile, err := os.Create("test_copy.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer newFile.Close()

    // Copy the bytes from source to destination
    bytesWritten, err := io.Copy(newFile, originalFile)
    if err != nil {
        log.Fatal(err)
    }
    log.Printf("Copied %d bytes.", bytesWritten)
    
    // Commit the file contents
    // Flushes memory to disk
    err = newFile.Sync()
    if err != nil {
    	log.Fatal(err)
    }
}