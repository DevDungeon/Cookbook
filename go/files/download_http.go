package main

import (
	"os"
	"io"
	"log"
	"net/http"
)

func main() {
	// Create output file
	newFile, err := os.Create("devdungeon.html")
	if err != nil {
		log.Fatal(err)
	}
	defer newFile.Close()

	// HTTP GET request devdungeon.com	
	url := "http://www.devdungeon.com/archive"
	response, err := http.Get(url)
	defer response.Body.Close()

	// Write bites from HTTP response to file
	numBytesWritten, err := io.Copy(newFile, response.Body)
	if err != nil {
		log.Fatal(err)
	}
	log.Printf("Downloaded %d byte file.\n", numBytesWritten)
}

