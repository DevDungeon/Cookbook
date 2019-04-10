import curses
import time

print("Preparing to initialize screen...")
curses.initscr()
print("Screen initialized.")

time.sleep(1)

print("Preparing to end window.")
curses.endwin()
print("Window ended.")