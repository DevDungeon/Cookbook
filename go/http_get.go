package main

import ("net/http"; "io"; "os"; "log"; "fmt")

func main() {
	resp, err := http.Get("http://example.com/")
	defer resp.Body.Close()
	n, err := io.Copy(os.Stdout, resp.Body)
	if err != nil { log.Fatal(err) }
	fmt.Println("Number of bytes copied to STDOUT:", n)
}