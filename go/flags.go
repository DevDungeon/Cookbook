package main

import (
	"flag"
	"fmt"
)

func main() {
	
	// Define flags
	// Flags can be used by any of the following:
	// -flag=X
	// -flag X
	// --flag X
	// --flag=X
	// The flag parser is smart enough to accomodate all cases
	maxp := flag.Int("max", 6, "the max value") // default 6

	// Parse
	// Takes all of the flags set previously, and assigns them all
	// pointers to their respective types.
	// Until this is called, the flag pointers are set to default
	// values or otherwise unexpected
	flag.Parse()

	// Use the flag values
	fmt.Printf("int max: %d\n", *maxp)
	
}