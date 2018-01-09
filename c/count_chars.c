#include <stdio.h>

main() {
	long num_chars;
	num_chars = 0;
	while (getchar() != EOF) {
		num_chars++;
	}
	printf("Character count: %ld\n", num_chars);
}
