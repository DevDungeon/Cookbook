/*
Copyright 2011 Google Inc.

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

/*
webmon is a simple website monitoring program.

It reads a JSON-formatted rule file like this:

[
	{"Host": "example.com", "Email": "admin@example.net"}
]

It periodically makes a GET request to http://example.com/.
If the request returns anything other than a 200 OK response, it sends an email
to admin@example.net. When the request starts returning 200 OK again, it sends
another email.

If a "Hook" field is present in a rule object, it will be executed as a shell
instruction on mail notification. For example, you might want to use this to
kill a flaky service. (Gross, but it works.)

Usage of webmon:
  -errors=3: number of errors before notifying
  -from="webmon@localhost": notification from address
  -hosts="": host definition file
  -poll=10s: file poll interval
  -smtp="localhost:25": SMTP server
  -timeout=10s: response read timeout

webmon was written by Andrew Gerrand <adg@golang.org>
*/
package main

import (
	"bytes"
	"encoding/json"
	"errors"
	"flag"
	"fmt"
	"log"
	"net"
	"net/http"
	"net/smtp"
	"os"
	"os/exec"
	"strings"
	"sync"
	"text/template"
	"time"
)

var (
	hostFile     = flag.String("hosts", "", "host definition file")
	pollInterval = flag.Duration("poll", time.Second*10, "file poll interval")
	fromEmail    = flag.String("from", "webmon@localhost", "notification from address")
	mailServer   = flag.String("smtp", "localhost:25", "SMTP server")
	numErrors    = flag.Int("errors", 3, "number of errors before notifying")
	readTimeout  = flag.Duration("timeout", time.Second*10, "response read timeout")
)

func main() {
	flag.Parse()
	log.Fatal(StartRunner(*hostFile, *pollInterval))
}

type Runner struct {
	sync.Mutex // Protects errors during concurrent Ping
	last       time.Time
	hosts      []*Host
	errors     map[string]*State
}

type Host struct {
	Host  string
	Email string
	Hook  string

	Error []error
}

type State struct {
	err  []error
	sent bool
}

func getWithTimeout(u string, timeout time.Duration) (*http.Response, error) {
	c := &http.Client{Transport: &http.Transport{
		Dial: func(n, addr string) (net.Conn, error) {
			c, err := net.Dial(n, addr)
			if err != nil {
				return nil, err
			}
			err = c.SetReadDeadline(time.Now().Add(timeout))
			if err != nil {
				return nil, err
			}
			return c, nil
		},
	}}
	return c.Get(u)
}

func (r *Runner) Ping(h *Host) error {
	u := fmt.Sprintf("http://%s/", h.Host)
	resp, err := getWithTimeout(u, *readTimeout)
	if err != nil {
		return r.Fail(h, err)
	}
	resp.Body.Close()
	if resp.StatusCode != 200 {
		return r.Fail(h, errors.New(resp.Status))
	}
	return r.OK(h)
}

func (r *Runner) OK(h *Host) error {
	r.Lock()
	s := r.errors[h.Host]
	if s == nil {
		r.Unlock()
		return nil
	}
	r.errors[h.Host] = nil
	r.Unlock()
	if !s.sent {
		return nil
	}
	h.Error = nil
	return h.Notify()
}

func (r *Runner) Fail(h *Host, getErr error) error {
	r.Lock()
	s := r.errors[h.Host]
	if s == nil {
		s = new(State)
		r.errors[h.Host] = s
	}
	r.Unlock()
	s.err = append(s.err, getErr)
	if s.sent || len(s.err) < *numErrors {
		return nil
	}
	s.sent = true
	h.Error = s.err
	return h.Notify()
}

var notifyTemplate = template.Must(template.New("").Funcs(template.FuncMap{
	"now": time.Now,
}).Parse(strings.TrimSpace(`
To: {{.Email}}
Subject: {{.Host}}

{{if .Error}}
{{.Host}} is down: {{range .Error}}{{.}}
{{end}}
{{else}}
{{.Host}} has come back up.
{{end}}
{{now}}
`)))

func (h *Host) Notify() error {
	if h.Hook != "" {
		cmd := exec.Command("bash", "-c", h.Hook)
		go func() {
			out, err := cmd.CombinedOutput()
			if err != nil {
				log.Printf("%s: hook: %v\n%s", h.Host, err, out)
			}
		}()
	}
	var b bytes.Buffer
	err := notifyTemplate.Execute(&b, h)
	if err != nil {
		return err
	}
	return SendMail(*mailServer, *fromEmail, []string{h.Email}, b.Bytes())
}

func StartRunner(file string, poll time.Duration) error {
	r := &Runner{errors: make(map[string]*State)}
	for {
		if err := r.loadRules(file); err != nil {
			return err
		}
		errc := make(chan error)
		for i := range r.hosts {
			go func(i int) {
				errc <- r.Ping(r.hosts[i])
			}(i)
		}
		for _ = range r.hosts {
			if err := <-errc; err != nil {
				log.Println(err)
			}
		}
		time.Sleep(poll)
	}
	panic("unreachable")
}

func (r *Runner) loadRules(file string) error {
	fi, err := os.Stat(file)
	if err != nil {
		return err
	}
	mtime := fi.ModTime()
	if !mtime.After(r.last) && r.hosts != nil {
		return nil
	}
	f, err := os.Open(file)
	if err != nil {
		return err
	}
	defer f.Close()
	var hosts []*Host
	err = json.NewDecoder(f).Decode(&hosts)
	if err != nil {
		return err
	}
	r.last = mtime
	r.hosts = hosts
	return nil
}

func SendMail(addr string, from string, to []string, msg []byte) error {
	c, err := smtp.Dial(addr)
	if err != nil {
		return err
	}
	if err = c.Mail(from); err != nil {
		return err
	}
	for _, addr := range to {
		if err = c.Rcpt(addr); err != nil {
			return err
		}
	}
	w, err := c.Data()
	if err != nil {
		return err
	}
	_, err = w.Write(msg)
	if err != nil {
		return err
	}
	err = w.Close()
	if err != nil {
		return err
	}
	return c.Quit()
}