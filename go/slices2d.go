package main

import (
	"fmt"
)

// MyGrid A 2D slice of bools
type MyGrid [][]bool

func makeGrid(numRows int, numCols int) *MyGrid {
	tempGrid := make(MyGrid, numRows) // Init bunch of empty slices
	for i := 0; i < numRows; i++ {
		tempGrid[i] = make([]bool, numCols)
	}
	return &tempGrid
}

func main() {
	var grid *MyGrid
	grid = makeGrid(3, 10)
	fmt.Printf("%v\n", grid)
}
