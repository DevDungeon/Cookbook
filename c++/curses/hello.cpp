// g++ hello.cpp -lncurses
#include <curses.h>

int main(int argc, char* argv[]) {
    initscr();
    addstr("Hello, world!\n");
    addstr("Press any key to continue...");
//    use_default_colors();

    refresh();
    getch();
    endwin();
    return 0;
}
