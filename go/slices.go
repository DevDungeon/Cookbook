package main

import (
	"fmt"
)

func main() {
	slices := make([]string, 0) // type, length, capacity
	
	slices = append(slices, "test")
	slices = append(slices, "test")
	slices = append(slices, "test")
	slices = append(slices, "test")
	
	fmt.Println(slices)

	newSlices := slices[1:3]
	fmt.Println(newSlices)
}