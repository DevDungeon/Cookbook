#include <ncurses.h>

int main() {

    initscr();
    cbreak();
//    keypad(stdscr, TRUE);

    // If you don't refresh before creating the windows,
    // they will never show up...
    refresh();

    WINDOW* win1 = newwin(10, 10, 5, 5); // 10x10@5,5
    WINDOW* win2 = newwin(5, 15, 12, 15); // 5x15@12,15


    box(win1, 0, 0);
    wborder(win2, '|', '|', '-', '-', '+', '+', '+', '+');

//    touchwin(win1);
//    touchwin(win2);
    wrefresh(win2);
    waddstr(win1, "hello?");
    addstr("hi");
    whline(win1, 'O', 3);

    wrefresh(win1);
    refresh();
    doupdate();
    getch();


    endwin();
    return 0;

}
