package main 

import (
	"encoding/json"
	"fmt"

)

type Message struct {
    Name string
    Body string
    Time int64
}

func main() {
	
	// Create struct
	msg := Message{"Alice", "Hello", 1294706395881547000}

	// Marshal struct to JSON []bytes
	jsonbytes, _ := json.Marshal(msg)

	// Test
	bytes := []byte(`{"Name":"Alice","Body":"Hello","Time":1294706395881547000}`)
	if string(jsonbytes) == string(bytes) {
		fmt.Println("Byte slices match.")
	}
	
	// Unmarshal JSON string to strcut
	json.Unmarshal(jsonbytes, &msg)


	fmt.Printf("jsonbytes type %T \n", jsonbytes)
	fmt.Printf("Message reconstructed to struct: %v", msg)


}