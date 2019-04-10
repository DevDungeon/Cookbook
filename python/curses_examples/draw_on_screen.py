import curses
import time


screen = curses.initscr()

screen.addstr(4, 10, "Hello from (4, 10)!")
screen.refresh()








time.sleep(2)
curses.endwin()
