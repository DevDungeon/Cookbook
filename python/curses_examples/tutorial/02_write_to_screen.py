import curses
import time

screen = curses.initscr()

# Update the buffer, adding text at different locations
screen.addstr(0, 0, "This string gets printed at position (0, 0)")
screen.addstr(3, 1, "Try Russian text: Привет")
screen.addstr(4, 4, "X")


# Update the screen with any changes made
screen.refresh()

time.sleep(4)
curses.endwin()
