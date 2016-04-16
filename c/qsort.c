#include <stdio.h>

void qsort(int values[], int left, int right) {
	int i, last;
	void swap(int values[], int i, int j);
	
	if (left >= right) {
		return;
	}
	
	swap(values, left, (left + right) / 2);
	last = left;
	for (i = left + 1; i <= right; i++) {
		if (values[i] < values[left]) {
			swap(values, ++last, i);
		}
	}
	swap(values, left, last);
	qsort(values, left, last - 1);
	qsort(values, last + 1, right);
}

void swap(int values[], int i, int j) {
	int temp = values[i];
	values[i] = values[j];
	values[j] = temp;
}

void print_array(int nums[], int len) {
	printf("Values: ");
	for (int i = 0; i < len; i++) {
		printf("%d, ", nums[i]);
	}
	printf("%d.\n", nums[len - 1]);
}

int main() {
	int nums[] = {10, 4, 2, 5, 77, 8, 3, 88, 4, 33};
	
	printf("Sizeof nums[]: %ld\n", sizeof(nums));
	printf("Sizeof int: %ld\n", sizeof(int));
	int array_len = sizeof(nums) / sizeof(int);
	print_array(nums, array_len);
	
	qsort(nums, 0, (sizeof(nums) / sizeof(int)));
	
	print_array(nums, array_len);
	return 0;
}
