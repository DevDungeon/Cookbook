#include <stdio.h>

/* Take the input and print out ASCII characters. Useful for finding strings
     in binary files. */
int main() {
	int ch;
    char last_char_was_whitespace = 0;

	while ((ch = getchar()) != EOF) {
		if (
			(ch >= 'a' && ch <= 'z')
			|| (ch >= 'A' && ch <= 'Z')
			|| (ch >= '0' && ch <= '9')
            //|| (ch == '\n' || ch == '\t' || ch == ' ')  
            //|| (ch == '\n' || ch == '\t' || ch == ' ')  
		) {
			printf("%c", ch);
		} else if (ch == '\n' || ch == '\t' || ch == ' ') {
            // Print only a single space if whitespace detected
            if (last_char_was_whitespace == 0) {
                printf(" ");
                last_char_was_whitespace = 1;
            } else {
                last_char_was_whitespace = 0;
            }
        }
	}
	return 0;
}
