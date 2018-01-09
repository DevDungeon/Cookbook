#include <stdio.h>

/* Print out the number of times each numeric digit is seen in the input 
     as well as white space and other characters */
int main() {
	int ch, i, num_white, num_other;
	int num_digits[10];

	num_white = num_other = 0;
	for (i = 0; i < 10; i++) {
		num_digits[i] = 0;
	}

	while ((ch = getchar()) != EOF) {

		if (ch >= '0' && ch <= '9') {
			num_digits[ch - '0']++;
		} else if (ch == ' ' || ch == '\n' || ch == '\t') {
			num_white++;
		} else {
			num_other++;
		}
	}

	printf("Digits: \n");
	for (i = 0; i < 10; i++) {
		printf(" %d\t%d\n", i, num_digits[i]);
	}
	printf("White space: %d\n", num_white);
	printf("Other: %d\n", num_other);

	return 0;
}
