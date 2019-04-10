# pip install windows-curses
import curses
import time

screen = curses.initscr()
y, x = screen.getmaxyx()
curses.endwin()

print(y, x)
