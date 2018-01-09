package main

import (
	"fmt"
	"log"

	"gopkg.in/mgo.v2"
	"gopkg.in/mgo.v2/bson"
)

type Domain struct {
	Name         string
	ParentDomain string
	Headers      []Header
}

type Header struct {
	Key   string
	Value string
}

func main() {
	session, err := mgo.Dial("localhost")
	if err != nil {
		panic(err)
	}
	defer session.Close()

	c := session.DB("test").C("domain")

	// Insert domain
	header := Header{"Server", "nginx"}
	headers := []Header{header}
	err = c.Insert(&Domain{"www.example.com", "www.demo.com", headers}, &Domain{Name: "www.test.com"})
	if err != nil {
		log.Fatal(err)
	}

	// Get one domain
	var result Domain
	err = c.Find(bson.M{"name": "www.example123123123.com"}).One(&result)
	if err != nil {
		if err == mgo.ErrNotFound {
			log.Println("Domain not found.")
		}
		log.Fatal(err)
	}
	fmt.Println("Domains:", result)

	// Get many domain
	var results []Domain
	err = c.Find(bson.M{"name": "www.example.com"}).All(&results)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Domains:", results)

	// Get a domain with that has a header value of "Gin" case insensitive (finds nginx)
	err = c.Find(bson.M{"headers": bson.M{"$elemMatch": bson.M{"value": bson.RegEx{"Gin", "i"}}}}).All(&results)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Domains:", results)

}
