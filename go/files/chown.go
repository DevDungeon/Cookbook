package main

import (
	"log"
	"os"
)

func main() {
	// Get your user id and group id 
	uid := os.Getuid()
	gid := os.Getgid()

	// Change ownership and group to your user
	// Root user and group id is 0 (would need sudo)
	err := os.Chown("test.txt", uid, gid)
	if err != nil {
		log.Fatal(err)
	}
}
