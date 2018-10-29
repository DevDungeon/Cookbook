package main

import (
	"os"
	"fmt"
	"log"
)

func main() {
	file, _ := os.Open("test.txt")
	defer file.Close()

	// Offset is how many bytes to move
	// Offset can be positive or negative
	var offset int64 = 5

	// Whence is the point of reference for offset
	// 0 = Beginning of file
	// 1 = Current 
	// 2 = End of file
	var whence int = 0
	newPosition, err := file.Seek(offset, whence)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Just moved to 5:", newPosition)

	newPosition, err = file.Seek(-2, 1)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Just moved back two:", newPosition)

	// Seek with no offset to your current position
	// to find out where you are currently
	currentPosition, err := file.Seek(0, 1)
	fmt.Println("Current position:", currentPosition)

	// Go to beginning of file
	newPosition, err = file.Seek(0, 0)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Position after seeking 0,0:", newPosition)
}
