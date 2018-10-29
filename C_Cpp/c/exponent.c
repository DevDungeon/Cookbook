#include <stdio.h>

/* Return the exponential value of a number */
long power(int base, int exp) {
	if (exp < 0) {
		printf("Error: This function does not handle negative exponents\n");
		return 0;
	} else {
		long total = 1;
		for (int i = 1; i <= exp; i++) {
			total = total * base;
		}
		return total;
	}
}

int main() {

	printf("Exponential values of 2.\n");
	printf("Base\tValue\t\n");
	for (int i = 0; i <= 32; i++) {
		printf("%d\t%ld\n", i, power(2, i));
	}

	return 0;
}
