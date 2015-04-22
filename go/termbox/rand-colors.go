package main

import (
	"github.com/nsf/termbox-go"
	"math/rand"
	"time"
)

// Draw random colored characters in every slot
func draw() {
	w, h := termbox.Size() // Get width/height
	termbox.Clear(termbox.ColorDefault, termbox.ColorDefault) // Clear
	// For whole screen, draw random colored block
	for y := 0; y < h; y++ {
		for x := 0; x < w; x++ {
			termbox.SetCell(x, y, ' ', termbox.ColorDefault,
				termbox.Attribute(rand.Int()%8)+1)
		}
	}
	termbox.Flush()
}

func main() {

	// Initialize termbox
	err := termbox.Init()
	if err != nil {	panic(err) }
	defer termbox.Close()

	// Create a channel to use later
	event_queue := make(chan termbox.Event)
	go func() {
		for {
			event_queue <- termbox.PollEvent()
		}
	}()

	// Draw random colors to screen
	draw()

	loop:
	for {
		select {
			// If channel sees ESC, break
			case ev := <-event_queue:
				if ev.Type == termbox.EventKey && ev.Key == termbox.KeyEsc {
					break loop
				}
			// No ESC, keep running as normal
			default:
				draw()
				time.Sleep(10 * time.Millisecond)
		}
	}
}
