// http_request_with_cookie.go
package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	request, err := http.NewRequest("GET", "https://www.devdungeon.com", nil)
	if err != nil {
		log.Fatal(err)
	}

	// Create a new cookie with the only required fields
	myCookie := &http.Cookie{
		Name:  "cookieKey1",
		Value: "value1",
	}

	// Add the cookie to your request
	request.AddCookie(myCookie)

	// Ask the request to tell us about itself,
	// just to confirm the cookie attached properly
	fmt.Println(request.Cookies())
	fmt.Println(request.Header)

	// Do something with the request
	// client := &http.Client{}
	// client.Do(request)
}
