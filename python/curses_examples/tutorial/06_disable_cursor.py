import curses
import time

screen = curses.initscr()

curses.curs_set(0)
screen.addstr(2, 2, "Hello, I disabled the cursor!")
screen.refresh()
time.sleep(4)

curses.curs_set(1)
screen.addstr(3, 2, "And now the cursor is back on.")
screen.refresh()
time.sleep(4)

curses.endwin()
