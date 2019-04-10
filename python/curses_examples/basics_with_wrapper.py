# https://docs.python.org/3.3/howto/curses.html
from curses import wrapper

# We just have to define a callable (a function) to pass to wrapper() and it will run and then restore terminal
# when it is done. It will also wrap it in a try/catch and re-raise.
def main(stdscr):
    # Clear screen
    stdscr.clear()

    x = 0
    for y in range(0, 3):
        stdscr.addstr(y, x, 'Add text to the screen.')

    stdscr.refresh()

    stdscr.addstr(4, 0, 'Press any key to exit.')
    stdscr.getkey()  # Just wait for a keypress before exiting

# Convenience function to handle the general boilerplate
wrapper(main)
