// Compile with
// gcc ncurses.c -lncurses

// If necessary install ncurses headers with 
// sudo apt-get install libncurses-dev
#include <ncurses.h>

int main() {
	initscr();
	clear();

	printw("Hello, world!");
	getch();

	endwin();
}
