package main

import (
	"bytes"
	"encoding/base64"
	"fmt"
	"image"
	"image/png"
)

func main() {
	// Create a blank image 10x20 pixels
	myImage := image.NewRGBA(image.Rect(0, 0, 10, 20))

	// In-memory buffer to store PNG image
	// before we base 64 encode it
	var buff bytes.Buffer

	// The Buffer satisfies the Writer interface so we can use it with Encode
	png.Encode(&buff, myImage)

	// Encode the bytes in the buffer to a base64 string
	encodedString := base64.StdEncoding.EncodeToString(buff.Bytes())

	// You can embed it in an html doc with this string
	htmlImage := "<img src=\"data:image/png;base64," + encodedString + "\" />"
	fmt.Println(htmlImage)
}
