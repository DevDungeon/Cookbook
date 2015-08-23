package main

import (
	"log"
	"os"
)

func main() {
	// Linux style octal rwx permissions
	err := os.Chmod("test.txt", 0777)
	if err != nil {
		log.Fatal(err)
	}

	
}
