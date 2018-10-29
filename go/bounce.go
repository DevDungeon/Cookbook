/*
Copyright 2013 Google Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

// Command bounce is a simple HTTP reverse proxy.
package main

import (
	"flag"
	"log"
	"net/http"
	"net/http/httputil"
	"net/url"
)

var (
	target   = flag.String("target", "", "Target URL")
	httpAddr = flag.String("http", ":9001", "HTTP Listen Address")
)

func main() {
	flag.Parse()
	if *target == "" {
		log.Fatal("must specify -target")
	}
	u, err := url.Parse(*target)
	if err != nil {
		log.Fatal(err)
	}
	p := &httputil.ReverseProxy{Director: func(r *http.Request) {
		p, q := r.URL.Path, r.URL.RawQuery
		*r.URL = *u
		r.URL.Path, r.URL.RawQuery = p, q
		r.Host = u.Host
	}}
	log.Fatal(http.ListenAndServe(*httpAddr, p))
}