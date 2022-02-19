package main
// Run with:
// go run portscan.go www.example.com

import (
	"time"
	"strconv"
	"log"
	"net"
	"os"
)

func printUsage() {
	log.Println("Usage: ")
	log.Println("  go run portscan.go <host> ")
	log.Println("Example: ")
	log.Println("  go run portscan.go www.example.com")
	log.Println("  go run portscan.go 8.8.8.8")
}

func testTcpConnect(host string, port int, doneChannel chan bool) {
	timeoutLength := 5 * time.Second
	conn, err := net.DialTimeout("tcp", host +":" + strconv.Itoa(port), timeoutLength)
	if err != nil {
		doneChannel <- false
		return // Could not connect
	} 
	conn.Close()
	log.Printf("[+] %d connected", port)
	doneChannel <- true
}

func main() {
	if len(os.Args) == 1 {
		log.Println("No arguments provided.")
		printUsage()
		os.Exit(1)
	}
	doneChannel := make(chan bool)
	activeThreadCount := 0
	log.Println("Scanning host: " + os.Args[1])
	for portNumber := 1; portNumber <= 65535; portNumber++ {
		activeThreadCount++
		go testTcpConnect(os.Args[1], portNumber, doneChannel)
	}

	for {
		<- doneChannel
		activeThreadCount--;
		if activeThreadCount == 0 {
			break
		}
	}
}