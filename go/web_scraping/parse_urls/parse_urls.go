// parse_urls.go
package main

import (
	"fmt"
	"log"
	"net/url"
)

func main() {
	// Parse a complex URL
	parsedUrl, err := url.Parse("https://www.example.com/path/../to/?query=123&this=that#fragment")
	if err != nil {
		log.Fatal(err)
	}

	// Print out URL pieces
	fmt.Println("Scheme: " + parsedUrl.Scheme)
	fmt.Println("Host: " + parsedUrl.Host)
	fmt.Println("Path: " + parsedUrl.Path)
	fmt.Println("Query string: " + parsedUrl.RawQuery)
	fmt.Println("Fragment: " + parsedUrl.Fragment)

	// Get the query key/values as a map
	fmt.Println("\nQuery values:")
	queryMap := parsedUrl.Query()
	fmt.Println(queryMap)

	// Craft a new URL from scratch
	var customURL url.URL
	customURL.Scheme = "https"
	customURL.Host = "google.com"
	newQueryValues := customURL.Query()
	newQueryValues.Set("key1", "value1")
	newQueryValues.Set("key2", "value2")
	customURL.Fragment = "bookmarkLink"
	customURL.RawQuery = newQueryValues.Encode()

	fmt.Println("\nCustom URL:")
	fmt.Println(customURL.String())
}
