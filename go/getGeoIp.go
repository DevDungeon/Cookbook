package main

import(
	"fmt"
	"net/http"
	"io/ioutil"
	"encoding/json"
)

type GeoIP struct {
	Ip string `json:"ip"`
	CountryCode string `json:"country_code"`
	CountryName string `json:"country_name""`
	RegionCode string `json:"region_code"`
	RegionName string `json:"region_name"`
	City string `json:"city"`
	Zipcode string `json:"zipcode"`
	Lat float32 `json:"latitude"`
	Lon float32 `json:"longitude"`
	MetroCode string `json:"metro_code"` 
	AreaCode string `json:"area_code"`
}

func main() {

	resp, err := http.Get("https://freegeoip.net/json/www.google.com")
	if err != nil { fmt.Println(err) }
	defer resp.Body.Close()
	
	// Read response body in to string, so I can unmarshal
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil { fmt.Println(err) }

	// Unmarshal response JSON to GeoIP struct
	var geo GeoIP
	err = json.Unmarshal(body, &geo)
	if err != nil { fmt.Println(err) }

	// Everything accessible now
	fmt.Println(geo.Ip)
	fmt.Println(geo.CountryCode)
	fmt.Println(geo.CountryName)
	fmt.Println(geo.Zipcode)
	fmt.Println(geo.Lat)
	fmt.Println(geo.Lon)
	fmt.Println(geo.MetroCode)
	fmt.Println(geo.AreaCode)

}
