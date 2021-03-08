#include <stdio.h>

int main() {
	int digits[10];
	
	printf("Uninitialized values of array.\nIndex\tValue\t\tPointer\n");
	for (int i = 0; i < 10; i++) {
		printf("%d\t%d\t\t%p\n", i, digits[i], &digits[i]);
	}

}
