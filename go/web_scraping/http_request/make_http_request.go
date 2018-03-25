// make_http_request.go
package main

import (
	"io"
	"log"
	"net/http"
	"os"
)

func main() {
	// Make HTTP GET request
	response, err := http.Get("https://www.devdungeon.com/")
	if err != nil {
		log.Fatal(err)
	}
	defer response.Body.Close()

	// Copy data from the response to standard output
	n, err := io.Copy(os.Stdout, response.Body)
	if err != nil {
		log.Fatal(err)
	}

	log.Println("Number of bytes copied to STDOUT:", n)
}
