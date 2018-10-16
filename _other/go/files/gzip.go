package main

import (
	"os"
	"compress/gzip"
	"log"
)

func main() {
	// Create .gz file to write to
	outputFile, err := os.Create("test.txt.gz")
	if err != nil {
		log.Fatal(err)
	}

	// Create a gzip writer on top of file writer
	gzipWriter := gzip.NewWriter(outputFile)
	defer gzipWriter.Close()

	// When we write to the gzip writer
	// it will in turn compress the contents
	// and then write it to the underlying
	// file writer as well
	// We don't have to worry about how all
	// the compression works since we just
	// use it as a simple writer interface
	// that we send bytes to
	_, err = gzipWriter.Write([]byte("Gophers rule!\n"))
	if err != nil {
		log.Fatal(err)
	}

	log.Println("Compressed data written to file.")	
}