import curses
import curses.textpad
import time
 
stdscr = curses.initscr()
 
#curses.noecho()
#curses.echo()
curses.noecho() 
 
begin_x = 20
begin_y = 7
height = 5
width = 40
win = curses.newwin(height, width, begin_y, begin_x)
tb = curses.textpad.Textbox(win)
text = tb.edit()
curses.addstr(4,1,text.encode('utf_8'))
 
#hw = "Hello world!"
#while 1:
# c = stdscr.getch()
# if c == ord('p'):
# elif c == ord('q'): break # Exit the while()
# elif c == curses.KEY_HOME: x = y = 0
 
curses.endwin()
