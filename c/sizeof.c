#include <stdio.h>

int main() {
	char c;
	short sh;
	int i;
	long l;
	printf("Size of:\nChar:\t%lu\nShort:\t%lu\nInt:\t%lu\nLong:\t%lu\n",
		sizeof(c), sizeof(sh), sizeof(i), sizeof(l));

	return 0;
}
