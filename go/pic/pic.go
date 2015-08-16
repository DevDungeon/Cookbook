package main

import "code.google.com/p/go-tour/pic"

// Pic matches a special definition expected in the pic package
func Pic(dx, dy int) [][]uint8 {
	slice := make([][]uint8, dy)

	for y := 0; y < dy; y++ {
		slice[y] = make([]uint8, dx)
		for x := 0; x < dx; x++ {
			slice[y][x] = uint8((x ^ y))
		}

	}
	return slice
}

func main() {
	// Show() accepts a function name
	pic.Show(Pic)
}
