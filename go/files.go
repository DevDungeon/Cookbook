package main

import (
	//"io"
	"fmt"
	"os"
)

func main() {

	// Check if file exists
	myfile, err := os.OpenFile("test.txt", os.O_APPEND, 0666)
	if err != nil {
		if os.IsNotExist(err) { // Special function to see if error was "file not exists"
			fmt.Println("Detected that file does not exist, going to create a new one!")
			myfile, err = os.Create("test.txt")
			if err != nil { // Error creating new file
				fmt.Println("Error creating new file: ", err)
			}
		}
	} else {
		fmt.Println("File exists and was opened with append mode.")
	}
	defer myfile.Close()

	// Write a string
	myfile.WriteString("Test!")

}
