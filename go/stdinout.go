package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	bio := bufio.NewReader(os.Stdin)
	for line, hasMoreInLine, err := bio.ReadLine(); err == nil; line, hasMoreInLine, err = bio.ReadLine() {
		if !hasMoreInLine {	}
		if err != nil { fmt.Println(err) }
		// Echo line back to STDOUT
		fmt.Printf("%s\n", line)
	}

}
