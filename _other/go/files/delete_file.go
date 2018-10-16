package main

import (
	"log"
	"os"
)

func main() {
	err := os.Remove("test.txt")
	if err != nil {
		log.Fatal(err)
	}
}
