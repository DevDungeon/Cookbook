package main

import (
	"github.com/nsf/termbox-go"
	"time"
	
)

// Draw text to specific coordinates
func drawText(x, y int, text string) {
	for _, letter := range text {
		// Can bitwise OR together multiple attributes
		termbox.SetCell(x, y, rune(letter), 
			termbox.ColorGreen | termbox.AttrBold , //fg
			termbox.ColorBlue) // bg
		x++
	}
	termbox.Flush()
}

func main() {

	// Initialize termbox
	err := termbox.Init()
	if err != nil {	panic(err) }
	defer termbox.Close()
	
	// Clear and set color. Screen seems to clear to default colors w/o this
	termbox.Clear(termbox.ColorGreen, termbox.ColorBlue) // fg,bg

	// Get width and height of screen
	w, h := termbox.Size()

	// Create a go routine with a channel to listen for keystrokes
	event_queue := make(chan termbox.Event)
	go func() {
		for {
			event_queue <- termbox.PollEvent()
		}
	}()

	// Writes a string to the screen. In the very bottom right
	// and auto adjusts depending on text length
	text := "Hello from the bottom right corner!"
	drawText(w - len(text), h-1, text)

	loop:
	for {
		select {
			// If channel sees ESC, break
			case ev := <-event_queue:
				if ev.Type == termbox.EventKey && ev.Key == termbox.KeyEsc {
					break loop
				}
				// movement keys
			// No ESC, keep running as normal
			default:
				drawText(0, 0, "Hello, world!")
				time.Sleep(10 * time.Millisecond)
		}
	}
}
