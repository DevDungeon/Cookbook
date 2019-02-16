package main

import (
    "fmt"
    "os"
    "os/signal"
    "syscall"
    "time" // or "runtime"
)

func main() {
  
    c := make(chan os.Signal, 1)
    signal.Notify(c, os.Interrupt)
    signal.Notify(c, syscall.SIGTERM)
   
    go func() {
        <-c
        fmt.Println("Sig caught")
        os.Exit(1)
    }()

    for {
        fmt.Println("sleeping...")
        time.Sleep(10 * time.Second) // or runtime.Gosched() or similar per @misterbee
    }
}