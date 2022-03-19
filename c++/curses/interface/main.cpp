#include <ncurses.h>
#include <iostream>
#include <bitset>

void redrawBorder() {
	clear();
	box(stdscr, 0, 0); // Redraw main border
	
}

int main() {

    initscr();
    mousemask(ALL_MOUSE_EVENTS, NULL);
    
    /**
     *  Colors
     */
    if (has_colors()) { start_color(); }
    //use_default_colors();
    init_pair(1, COLOR_CYAN, COLOR_BLACK);
    init_pair(2, COLOR_WHITE, COLOR_RED);
        
    cbreak();
    keypad(stdscr, TRUE);
    nonl();         /* tell curses not to do NL->CR/NL on output */
    noecho();
    curs_set(0);
    
    attrset(COLOR_PAIR(1));
	redrawBorder();
    //refresh();
    
    
    
    // short id;         /* ID to distinguish multiple devices */
    // int x, y, z;      /* event coordinates */
    // mmask_t bstate;   /* button state bits */

    while (true) {
	    int c = getch();
	    switch (c) {
			case 'q':
				endwin();
				exit(0);
			case KEY_MOUSE:
				MEVENT event;
				if (getmouse(&event) == OK) {
					clear();
					redrawBorder();
					
					attrset(COLOR_PAIR(2));
					mvaddstr(5, 5, std::to_string(event.x).c_str());
					mvaddstr(6, 5, std::to_string(event.y).c_str());
					mvaddstr(7, 5, "Mouse bitset: ");
					addstr(std::bitset<32>(event.bstate).to_string().c_str());
					if (event.bstate & BUTTON1_PRESSED) {
						addstr(" - Button 1 pressed");
					} else if (event.bstate & BUTTON1_DOUBLE_CLICKED) {
						addstr(" - Button 1 dclick");
					}
					attrset(COLOR_PAIR(1));
					
				}
				break;
				
				/**
				BUTTON1_PRESSED          mouse button 1 down
				BUTTON1_RELEASED         mouse button 1 up
				BUTTON1_CLICKED          mouse button 1 clicked
				BUTTON1_DOUBLE_CLICKED   mouse button 1 double clicked
				BUTTON1_TRIPLE_CLICKED   mouse button 1 triple clicked
				BUTTON2_PRESSED          mouse button 2 down
				BUTTON2_RELEASED         mouse button 2 up
				BUTTON2_CLICKED          mouse button 2 clicked
				BUTTON2_DOUBLE_CLICKED   mouse button 2 double clicked
				BUTTON2_TRIPLE_CLICKED   mouse button 2 triple clicked
				BUTTON3_PRESSED          mouse button 3 down
				BUTTON3_RELEASED         mouse button 3 up
				BUTTON3_CLICKED          mouse button 3 clicked
				BUTTON3_DOUBLE_CLICKED   mouse button 3 double clicked
				BUTTON3_TRIPLE_CLICKED   mouse button 3 triple clicked
				BUTTON4_PRESSED          mouse button 4 down
				BUTTON4_RELEASED         mouse button 4 up
				BUTTON4_CLICKED          mouse button 4 clicked
				BUTTON4_DOUBLE_CLICKED   mouse button 4 double clicked
				BUTTON4_TRIPLE_CLICKED   mouse button 4 triple clicked
				BUTTON_SHIFT             shift was down during button state change
				BUTTON_CTRL              control was down during button state change
				BUTTON_ALT               alt was down during button state change
				ALL_MOUSE_EVENTS         report all button state changes
				REPORT_MOUSE_POSITION    report mouse movement
				*/ 
				
			case KEY_RESIZE:
				redrawBorder();
				mvaddstr(10, 10, "Window resized");
				break;
				
			default:
				break;
		}
	 }



	/**
	 * Cleanup and shutdown
	 */
    endwin();
    return 0;
}
