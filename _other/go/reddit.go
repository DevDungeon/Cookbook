package main

import (
	"encoding/json"
	"errors"
	"fmt"
	"log"
	"net/http"
)

// Item to hold reddit response subitem
type Item struct {
	Title    string
	URL      string
	Comments int `json:"num_comments"`
}

// Struct to hold entire reddit response
type Response struct {
	Data struct {
		Children []struct {
			Data Item
		}
	}
}

// Stringer method for Item struct
func (i Item) String() string {
	return fmt.Sprintf("%s\n%s\n%d\n", i.Title, i.URL, i.Comments)
}

// Main
func main() {

	items, err := Get("golang")
	if err != nil {
		log.Fatal(err)
	}
	for _, item := range items {
		fmt.Println(item)
	}

}

// Get reddit response items by subreddit
func Get(reddit string) ([]Item, error) {
	url := fmt.Sprintf("http://reddit.com/r/%s.json", reddit)
	resp, err := http.Get(url)
	if err != nil {
		return nil, err
	}
	// Run close at end of function, wherever it exits.
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return nil, errors.New(resp.Status)
	}
	r := new(Response)
	err = json.NewDecoder(resp.Body).Decode(r)
	if err != nil {
		return nil, err
	}
	items := make([]Item, len(r.Data.Children))
	for i, child := range r.Data.Children {
		items[i] = child.Data

	}
	return items, nil
}
