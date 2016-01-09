package main

import (
	"fmt"
	"os/user"
)

func main() {
	fmt.Println(user.Current())
}
