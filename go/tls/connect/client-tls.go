package main

import (
	"crypto/tls"
	"log"

)

func main() {
	
	// Dial a TLS server, without verification
	config := tls.Config{InsecureSkipVerify: true}
	conn, err := tls.Dial("tcp", "localhost:8080", &config)
	if err != nil { log.Print(err) }
	defer conn.Close()
	
}