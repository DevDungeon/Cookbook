#include <stdio.h>
#include <stdlib.h>
/* Copy a file, but only copy the first n bytes */


// while getchar is not eof and limit not reached
// putchar
int main(int argc, char **argv) {

	if (argc < 2) {
		printf("Not enough arguments. Example usage:\n  subcopy 25 < input.txt > output.txt\n");
		return 1;
	}
	int ch;
	int limit = atoi(argv[1]);
	for (int i = 0; i < limit && (ch = getchar()) != EOF; i++) {
		putchar(ch);
	}
	return 0;
}
