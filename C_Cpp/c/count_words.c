#include <stdio.h>

#define IN_WORD 1
#define OUT_OF_WORD 0


int main() {
	int ch, num_words, num_lines, num_chars, state;
	num_words = num_lines = num_chars = 0;
	while ((ch = getchar()) != EOF) {
		num_chars++;
		if (ch == '\n') {
			num_lines++;
		}
		if (ch == ' ' || ch == '\n' || ch == '\t') {
			state = OUT_OF_WORD;
		} else if (state == OUT_OF_WORD) {
			state = IN_WORD;
			num_words++;
		}
	}
	printf("Chars\tWords\tLines\n%d\t%d\t%d\n", num_chars, num_words, num_lines);
	return 0;
}
