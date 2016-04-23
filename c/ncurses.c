// Compile with
// gcc ncurses.cpp -lncurses

// If necessary install ncurses headers with 
// sudo apt-get install libncurses-dev
#include <ncurses.h>
#include <string.h>

int main() {
    initscr();
    clear();

    printw("Hello, world!");

    // Centering and placing text in specific places
    int row, col;
    char mesg[] = "Centered!";
    getmaxyx(stdscr, row, col);        /* get the number of rows and columns */
    mvprintw(row / 2, (col - strlen(mesg)) / 2, "%s", mesg);
    mvprintw(row - 2, 0, "This screen has %d rows and %d columns\n", row, col);
    mvaddch(3, 10, '!');

    // Colors
    if (has_colors() == FALSE) {    
        return(1);
    }
    start_color();
    init_pair(1, COLOR_RED, COLOR_BLACK);
    attron(COLOR_PAIR(1));
    mvprintw(1, 1, "Viola !!! In color ...");
    attroff(COLOR_PAIR(1));

    // Get characterrs and arrow keys
    keypad(stdscr, TRUE); // Enable the keypad on side
    getch();
    //int c = getch();
    //if (c == KEY_LEFT) {}

    endwin();
}


/* // Resizing
#include <signal.h>

void do_resize(int dummy)
{
}

int main(...)
{
signal(SIDWINCH, do_resize);
}
*/