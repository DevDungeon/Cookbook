#include <stdio.h>

/* Take the input and print out ASCII characters. Useful for finding strings
     in binary files. */
int main() {
	int ch;

	while ((ch = getchar()) != EOF) {
		if (
			(ch >= 'a' && ch <= 'z')
			|| (ch >= 'A' && ch <= 'Z')
			|| (ch >= '0' && ch <= '9')
			|| (ch == '\n' || ch == '\t' || ch == ' ')  
		) {
			printf("%c", ch);
		}
		
	}
	return 0;
}
