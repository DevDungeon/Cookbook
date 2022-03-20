/*
 * main.cpp
 * 
 * Copyright 2022 odin <odin@bdeb>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


//#include <iostream>
#include <curses.h>
#include <sstream>
#define col1offset 4

void setup_color() {
	if (has_colors()) start_color();
    init_pair(1, COLOR_CYAN, COLOR_BLACK);
    init_pair(2, COLOR_WHITE, COLOR_RED);
    attrset(COLOR_PAIR(1));
}

void init_curses() {
	initscr(); // Initialize curses
	cbreak();  // Do not buffer input until newline
	keypad(stdscr, TRUE); // Allow function keys and arrows
	noecho(); // Do not print keypresses
	nonl(); // Do not newline on input
	curs_set(0); // Hide/show cursor
	mousemask(ALL_MOUSE_EVENTS, NULL); // Listen for all mouse events
	setup_color();
}

int main(int argc, char **argv)
{
	init_curses();
	box(stdscr, 0, 0);
	/* more setup */
	int maxY, maxX;
	int tempY, tempX;
	getmaxyx(stdscr, maxY, maxX);
	std::stringstream str_buffer;
	
	//move(0, 3);
	//str_buffer << "Terminal size: " << maxY << ',' << maxY;
	//addstr(str_buffer.str().c_str());
	////getyx(stdscr, tempY,tempX);
	
	
	/* Draw the ASCII data */
	move(2,2);
	addstr("Decimal Hex   Char");
	getyx(stdscr, tempY,tempX);
	move(++tempY, col1_offset);
	
	for (int i = 0; i < 8; i++) {
		if (isprint(i)) addch(i);
		else addch (' ');
		move(++tempY, col1_offset);
	}
	move(3, 2);
	
	
	move(++tempY, 3);
	for (int i = 0; i < 256; i++) {
		addch(i);
		getyx(stdscr, tempY, tempX);
		if (tempX == maxX-3) {
			move(tempY+1, 3);
		}
	}
	
	
	if (move(maxY-1, 3) == OK) refresh(); else { endwin(); exit(1); }
	
	
	addstr("Press q to exit");
	while (getch() != 'q') continue;
	endwin();
	return 0;
}

