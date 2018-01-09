#include <stdio.h>

/* Returns the number of 1 bits in an int */
int bitcount(unsigned x) {
	int b;
	for (b = 0; x != 0; x >>= 1) {
		if (x & 01) {
			b++;
		}
	}
	return b;
}

main() {
	printf("On bit counts:\n");
	for (int i = 0; i < 25; i++) {
		printf("%d: %d\n", i, bitcount(i));
	}
}
