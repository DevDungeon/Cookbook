import curses
import time

screen = curses.initscr()

# Get current size
y, x = screen.getmaxyx()

# See if a resize would succeed
y = 30
x = 100
can_resize = curses.is_term_resized(y, x)

# Action in loop if resize is True:
if can_resize:
    screen.clear()
    curses.resizeterm(y, x)
    screen.refresh()
    time.sleep(3)
else:
    screen.endwin()
    print("Unable to resize window")
