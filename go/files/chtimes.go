package main

import (
	"os"
	"time"
)

func main() {
	twoDaysFromNow := time.Now().Add(48 * time.Hour)
	lastAccessTime := twoDaysFromNow
	lastModifyTime := twoDaysFromNow

	// Set last read and write times to 2 days ahead
	os.Chtimes("test.txt", lastAccessTime, lastModifyTime)
}