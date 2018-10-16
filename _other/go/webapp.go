package main

import (
	"net/http"
	"io"
)

func main() {
	
	// Route http request
	http.HandleFunc("/myform", myForm)
	http.HandleFunc("/mypost", handlePost)
	// Run a web server connecting to a port
    http.ListenAndServe(":9000", nil)

	
	// Take in form input
	// return json of form input
	
}


func handlePost(res http.ResponseWriter, req *http.Request) {
	// Do something with form data
	postedText := req.FormValue("mytext")

	res.Header().Set("Content-Type", "text/html")
	io.WriteString(res, postedText)
}

func myForm(res http.ResponseWriter, req *http.Request) {
    res.Header().Set(
        "Content-Type", 
        "text/html",
    )
    io.WriteString(
        res, 
		`<doctype html>
		<html>
		    <head>
		        <title>Web Form</title>
		    </head>
		    <body>
		        <form method="POST" action="/mypost">
		        	<input type="text" name="mytext" />
		        	<input type="submit" name="submit" value="submit" />
		        </form>
		    </body>
		</html>`,
    )
}