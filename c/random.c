#include <time.h>
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv) {
	srand(time(0));
	printf("%d\n", rand());
	return 0;
}
