package main 

import (
	"fmt"
	"sync"
)


type URLStore struct {
	urls map[string]string
	mu sync.RWMutex
}


func NewURLStore() *URLStore {
	return &URLStore {
		urls: make(map[string]string),
	}
}

func (s *URLStore) Get(key string) string {
	s.mu.RLock()
	defer s.mu.RUnlock()
	return s.urls[key]
}

func (s *URLStore) Set(key, url string) bool {
	s.mu.Lock()
	defer s.mu.Unlock()
	_, present := s.urls[key]
	if present {
		return false
	}
	s.urls[key] = url
	return true
}

func Redirect(w http.ResponseWriter)

func main() {

	s := NewURLStore()
	s.Set("zvza", "http://www.zvza.net")
	url := s.Get("zvza")
	fmt.Println(url)

}
