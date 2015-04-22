package main

import (
	"fmt"
)

func main() {
	// for y years, compoung interest i on 
	// seed s
	s := 10000.00	// seed money
	i := 1.05	// interest
	y := 10		// num years
	total := s;	// total money
	for n := 0; n < y; n++ {
		total = i * total
		fmt.Printf("Year: %d - %f\n", n, total)
	}
	fmt.Printf("$%f at %f interest over %d years\n", s, i, y)
	fmt.Println(total)
}
