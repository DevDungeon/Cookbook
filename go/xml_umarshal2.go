package main

import "fmt"
import "encoding/xml"

var data string = `
<table>
    <name>
        <code>23764</code>
        <name>Smith, Jane</name>
    </name>
    <name>
        <code>11111</code>
        <name>Doe, John</name>
    </name>
</table>
`

type Customer struct {
    Code string `xml:"code"`
    Name string `xml:"name"`
}

type Customers struct {
    Customers []Customer `xml:"name"`
}

func main() {
	var custs Customers
	err := xml.Unmarshal([]byte(data), &custs)
	
	if err != nil {
		fmt.Println(err)
	}

    fmt.Printf("%v", custs)
}