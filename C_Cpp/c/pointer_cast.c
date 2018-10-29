#include <stdio.h>

int main() {
	void *voidptr;
	int x = 1;
	voidptr = &x;

	printf("%d - %p\n", *(int *)voidptr, voidptr);

	return 0;
}
