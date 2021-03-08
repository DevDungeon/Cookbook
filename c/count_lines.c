#include <stdio.h>

int main() {
	long line_count;
	int ch;
	while ((ch = getchar()) != EOF) {
		if (ch == '\n') {
			line_count++;
		}
	}
	printf("Line count: %ld\n", line_count);

	return 0;
}
