// login_to_site.go
package main

import (
	"fmt"
	"log"
	"net/http"
	"net/url"
)

func main() {
	//loginUrl := "https://<website>/login.php"
	user := "myUsername"
	password := "myPassword123"

	loginUrl := "https://httpbin.org/cookies/set?name=test&pass=pass123"

	response, err := http.PostForm(
		loginUrl,
		url.Values{
			"name": {user},
			"pass": {password},
		},
	)
	if err != nil {
		log.Fatal(err)
	}
	defer response.Body.Close()

	fmt.Println("Response cookies: ", response.Cookies())
	fmt.Println("Response headers: ", response.Header)

	request, err := http.NewRequest("GET", "https://www.devdungeon.com/admin/reports/status", nil)
	if err != nil {
		log.Fatal(err)
	}

	// Use the cookies that the response provided
	for _, cookie := range response.Cookies() {
		request.AddCookie(cookie)
	}

	// Ask the request to tell us about itself,
	// just to confirm the cookie attached properly
	fmt.Println(request.Cookies())
	fmt.Println(request.Header)

	// Do something with the request
	client := &http.Client{}
	response, err = client.Do(request)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Response cookies:", response.Cookies())
	fmt.Println("Response headers:", response.Header)
	//_, err = io.Copy(os.Stdout, response.Body)
	if err != nil {
		log.Fatal(err)
	}

	// Note you might get multiple Set-Cookie headers, you have to determine which one is the right session cookie, or use all of them. You can combine multiple key/value pairs by separating them with a semicolon. A web browser by default would combine all the cookies provided in to one long string
	// you can string.join"; " them or use a special cookie class? https://golang.org/src/net/http/cookie.go
	// ex. set("Cookie", "PHPSESSID=zcvzcvx; something_else=123; this=42")

}
