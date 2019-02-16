
package main

import (
	"log"
	"io/ioutil"
)

func main() {
	// Read file to byte slice
	data, err := ioutil.ReadFile("test.txt")
	if err != nil {
		log.Fatal(err)
	}

	log.Printf("Data read: %s\n", data)
}
