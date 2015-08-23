package main

import (
	"os"
	"log"
	"fmt"
)

func main() {
	// Create a hard link
	// You will have two file names that point to the same contents
	// Changing the contents of one will change the other
	// Deleting/renaming one will not affect the other
	err := os.Link("original.txt", "original_also.txt")
	if err != nil {
		log.Fatal(err)
	}
	

fmt.Println("creating sym")
	// Create a symlink
	err = os.Symlink("original.txt", "original_sym.txt")
	if err != nil {
		log.Fatal(err)
	}

	// Lstat will return file info, but if it is actually
	// a symlink, it will return info about the symlink.
	// It will not follow the link and give information
	// about the real file
	// Symlinks do not work in Windows
	fileInfo, err := os.Lstat("original_sym.txt")
	if err != nil {
		log.Fatal(err)
	}
  	fmt.Printf("Link info: %+v", fileInfo)

	// Change ownership of a symlink only 
	// and not the file it points to
	err = os.Lchown("original_sym.txt", os.Getuid(), os.Getgid())
	if err != nil {
		log.Fatal(err)
	}
}
