import curses
from curses import ascii
import time

# These are some basic functions
# It is recommended to use the curses.wrapper() to handle all of the boilerplate instead

# This will create a new screen and replace the console with the cursor in top left
# The original terminal screen still exists behind/underneath and will be put back
screen = curses.initscr()

# Allow multibye keys like curses.KEY_LEFT
screen.keypad(1)  # screen.keypad(0) to disallow

# React to keys instantly instead of buffering and returning after enter is pressed
curses.cbreak()  # curses.nocbreak() to set it back

# Don't echo keys to screen when pressed
curses.noecho()  # curses.echo() to set it back

# Hide the cursor
curses.curs_set(0)


# Get the window size. In this case the window is whole screen
size = screen.getmaxyx()
screen.addstr(0,0, "Terminal size" + repr(size))
screen.refresh()
time.sleep(2)


screen.addstr(3, 10, 'Text on line 3 char 10')

# Get cursor positions
yx = curses.getsyx()
screen.addstr(4, 10, 'Cursor position:' + repr(yx))

screen.refresh()

time.sleep(2)
screen.clear()

# Color text
curses.start_color()
screen.addstr("Pretty text", curses.color_pair(1))
screen.refresh()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
screen.addstr(0,0, "RED ALERT!", curses.color_pair(1))
screen.refresh()

# A_BLINK	Blinking text # doesn't work well
# A_BOLD	Extra bright or bold text
# A_DIM	Half bright text
# A_REVERSE	Reverse-video text
# A_STANDOUT	The best highlighting mode available
# A_UNDERLINE	Underlined text
screen.addstr(1, 0, "Normal")
screen.addstr(2, 0, "Blink?!", curses.A_BLINK)
screen.addstr(3, 0, "Bold?!", curses.A_BOLD)
screen.addstr(4, 0, "Dim?!", curses.A_DIM)
screen.addstr(5, 0, "Reverse?!", curses.A_REVERSE)
screen.addstr(6, 0, "Standout?!", curses.A_STANDOUT)
screen.addstr(7, 0, "Underline?!", curses.A_UNDERLINE)
screen.refresh()


screen.addstr(8, 0, "Press any key to exit")
# getkey/getch will refresh the window before waiting
c = screen.getkey()  # or getch(), getwch()

curses.endwin()

if curses.ascii.isalpha(c):
    print("You pressed an alphabet character!")
else:
    print("You pressed a non-alpha character to exit!")
print(c)

# curses.ascii.isalnum(c)
# curses.ascii.isalpha(c)
# curses.ascii.isascii(c)
# curses.ascii.isblank(c)
# curses.ascii.isdigit(c)
# curses.ascii.ispunct(c)
# curses.ascii.isspace(c)
# curses.ascii.islower(c)
# curses.ascii.isupper(c)
# curses.ascii.isgraph(c) # Is it a graphical (visible) value
