package main

import (
	"log"
	"net"
	"crypto/tls"
)

func main() {

	// Load cert and key for server to use
	cert, err := tls.LoadX509KeyPair("server.crt", "server.key")
	if err != nil {
		log.Fatalf("Could not load cert/key: %s", err)
	}

	// Configure and run the TLS listen server
	config := tls.Config{Certificates: []tls.Certificate{cert}}
	host := "0.0.0.0:8080"
	listener, err := tls.Listen("tcp", host, &config)
	if err != nil {
		log.Fatalf("Could not set up listener: %s", err)
	}
	log.Printf("Listening on %s for TLS", host)

	// Infinite loop to listen and handle connections
	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Printf("Error during accept: %s", err)
			break
		}
		defer conn.Close()
		log.Printf("Accepted from: %s", conn.RemoteAddr())
		go handleClient(conn)
	}
}


// Return a simple HTTP 200 OK response for a web browser to understand
func handleClient(c net.Conn) {
	c.Write([]byte("HTTP-1.1 200 OK\n\ntest"))
	c.Close()
}