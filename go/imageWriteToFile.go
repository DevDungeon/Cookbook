package main

import (
	"image"
	"image/png"
	"os"
)

func main() {
	// Create a blank image 100x200 pixels
	myImage := image.NewRGBA(image.Rect(0, 0, 100, 200))
	myImage.Pix[3] = 255

	// outputFile is a File which satisfies the Writer interface
	outputFile, err := os.Create("test.png")
	if err != nil {
		// Handle error
	}

	// Encode takes a writer interface and an image interface
	// We pass it the File and the RGBA
	png.Encode(outputFile, myImage)

	// Don't forget to close files
	outputFile.Close()
}
