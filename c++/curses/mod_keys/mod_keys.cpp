			// int c = getch();
			// switch (c)
			case ctrl('j'): // #define ctrl(x) ((x) & 0x1f)
				addstr("ctrl j detected");
				break;
			default:
				if (c == KEY_ENTER) {
					addstr("Keypad enter pressed.");
				}
				if (c == 27) { // Alt key was down when key pressed
					// Get the next char that came with the alt
					c = getch();
					addstr("Alt/escaped key pressed: ");
					addch(c); // could be 'a' or 'A' if alt+shift
				}

