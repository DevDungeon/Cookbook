import curses

# Author: Nikolai Tschacher
# Date: 02.06.2013

class BoxSelector:
    """ Originally designed for accman.py.
        Display options build from a list of strings in a (unix) terminal.
        The user can browser though the textboxes and select one with enter.
    """
    
    def __init__(self, L):
        """ Create a BoxSelector object. 
            L is a list of strings. Each string is used to build 
            a textbox.
        """
        self.L = L
        # Element parameters. Change them here.
        self.TEXTBOX_WIDTH = 50
        self.TEXTBOX_HEIGHT = 6

        self.PAD_WIDTH = 400
        self.PAD_HEIGHT = 10000
        
    def pick(self):
        """ Just run this when you want to spawn the selction process. """
        self._init_curses()
        self._create_pad()
        
        windows = self._make_textboxes()
        picked = self._select_textbox(windows)
        
        self._end_curses()
        
        return picked
        
    def _init_curses(self):
        """ Inits the curses appliation """
        # initscr() returns a window object representing the entire screen.
        self.stdscr = curses.initscr()
        # turn off automatic echoing of keys to the screen
        curses.noecho()
        # Enable non-blocking mode. Keys are read directly, without hitting enter.
        curses.cbreak()
        # Disable the mouse cursor.
        curses.curs_set(0)
        self.stdscr.keypad(1)
        # Enable colorous output.
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
        self.stdscr.bkgd(curses.color_pair(2))
        self.stdscr.refresh()

    def _end_curses(self):
        """ Terminates the curses application. """
        curses.nocbreak()
        self.stdscr.keypad(0)
        curses.echo()
        curses.endwin()
        
    def _create_pad(self):
        """ Creates a big self.pad to place the textboxes in. """
        self.pad = curses.newpad(self.PAD_HEIGHT, self.PAD_WIDTH)
        self.pad.box()
        
    def _make_textboxes(self):
        """ Build the textboxes in the pad center and put them in the 
            horizontal middle of the pad. """
        # Get the actual screensize.
        maxy, maxx = self.stdscr.getmaxyx()
        
        windows = []
        i = 1
        for s in self.L:
            windows.append(self.pad.derwin(self.TEXTBOX_HEIGHT,
                    self.TEXTBOX_WIDTH, i, self.PAD_WIDTH//2-self.TEXTBOX_WIDTH//2))
            i += self.TEXTBOX_HEIGHT
            
        for k in range(len(windows)):
            windows[k].box()
            windows[k].addstr(4, 4, '0x{0:X} - {1}'.format(k, self.L[k]))
            
        return windows

    def _center_view(self, window):
        """ Centers and aligns the view according to the window argument given. 
            Returns the (y, x) coordinates of the centered window. """
        # The refresh() and noutrefresh() methods of a self.pad require 6 arguments
        # to specify the part of the self.pad to be displayed and the location on
        # the screen to be used for the display. The arguments are pminrow,
        # pmincol, sminrow, smincol, smaxrow, smaxcol; the p arguments refer
        # to the upper left corner of the self.pad region to be displayed and the
        # s arguments define a clipping box on the screen within which the
        # self.pad region is to be displayed.
        cy, cx = window.getbegyx()
        maxy, maxx = self.stdscr.getmaxyx()
        self.pad.refresh(cy, cx, 1, maxx//2 - self.TEXTBOX_WIDTH//2, maxy-1, maxx-1)
        return (cy, cx)
        
    def _select_textbox(self, windows):
        # See at the root textbox.
        topy, topx = self._center_view(windows[0])
        
        current_selected = 0
        last = 1
        top_textbox = windows[0]
        
        while True:
            # Highligth the selected one, the last selected textbox should
            # become normal again.
            windows[current_selected].bkgd(curses.color_pair(1))
            windows[last].bkgd(curses.color_pair(2))
            
            # While the textbox can be displayed on the page with the current 
            # top_textbox, don't alter the view. When this becomes impossible, 
            # center the view to last displayable textbox on the previous view.
            maxy, maxx = self.stdscr.getmaxyx()
            cy, cx = windows[current_selected].getbegyx()
            
            # The current window is to far down. Switch the top textbox.
            if ((topy + maxy - self.TEXTBOX_HEIGHT) <= cy):
                top_textbox = windows[current_selected]
            
            # The current window is to far up. There is a better way though...
            if topy >= cy + self.TEXTBOX_HEIGHT:
                top_textbox = windows[current_selected]
            
            if last != current_selected:
                last = current_selected
                
            topy, topx = self._center_view(top_textbox)
            
            c = self.stdscr.getch()
            
            # Vim like KEY_UP/KEY_DOWN with j(DOWN) and k(UP).
            if c == ord('j'):
                if current_selected >= len(windows)-1:
                    current_selected = 0 # wrap around.
                else:
                    current_selected += 1
            elif c == ord('k'):
                if current_selected <= 0:
                    current_selected = len(windows)-1 # wrap around.
                else:
                    current_selected -= 1
            elif c == ord('q'): # Quit without selecting.
                break
            # At hitting enter, return the index of the selected list element.
            elif c == curses.KEY_ENTER or c == 10:
                return int(current_selected)


if __name__ == '__main__':
    # As simple as that.
    L = [
         'I wish I was a wizard',
         'Sometimes it all just makes sense',
         'This string is here because I need it',
         'Being or not being!',
         'Python is worse then PHP ;)',
         'a -> b <=> if a then b'
        ]
        
    choice = BoxSelector(L).pick()
    print('[+] Your choice was "{0}"'.format(L[choice]))
