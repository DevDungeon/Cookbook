package main

import (
	"log"
	"os"
)

func main() {
	originalPath := "test.txt"
	newPath := "test2.txt"
	err := os.Rename(originalPath, newPath)
	if err != nil {
		log.Fatal(err)
	}
}
