package main

import(
	"fmt"
	"net/http"
	"io/ioutil"
	"encoding/json"
	"strings"
)

func main() {
	resp, err := http.Get("https://freegeoip.net/json/www.netdungeon.com")
	if err != nil { fmt.Println(err) }
	defer resp.Body.Close()
	
	// Read response body in to string
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil { fmt.Println(err) }

	//fmt.Printf("Body is of type %T\n%v\n%s", body, body, body)

	// Create a map of strings to the raw json messages
	var objmap map[string]*json.RawMessage
	err = json.Unmarshal(body, &objmap)
	if err != nil { fmt.Println(err) }
	fmt.Println(string(*objmap["city"])) 
	// The above is OK, but it prints the city with quotes "Houston"
	// We COULD use strings.Trim() to trim the quotes
	fmt.Println(strings.Trim(string(*objmap["city"]), "\""))
	
	// But it would be better to properly Unmarshal the data to a var
	var city string
	err = json.Unmarshal(*objmap["city"], &city)
	if err != nil { fmt.Println(err) }
	fmt.Println(city) // Prints a nice clean string with no quotes

}