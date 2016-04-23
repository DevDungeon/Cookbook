#include <stdio.h>

/* Print Fahrenheit-Celsius table */
main() {
	int fahr, celsius;
	int lower, upper, step;

	printf("Fahr\tCelsius\n");

	lower = 0;
	upper = 300;
	step = 20;

	fahr = 0;
	while (fahr <= upper) {
		celsius = 5 * (fahr - 32) / 9;
		printf("%d\t%d\n", fahr, celsius);
		fahr = fahr + step;
	}
}

