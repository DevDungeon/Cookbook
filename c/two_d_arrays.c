#include <stdio.h>

/* When accepting a 2d array as a function parameter, only the size of the right most array must be defined. */
void test_func1(int array1[][13]) {
    return;
}

/* This is equivalent of above. The parenthesis are necessary because the [] operator takes
 * precedence over the * operator. Without parenthesis this would be 13 int pointers in one array. */
void test_func2(int (*array2)[13]) {
    return;
}

int main() {
    /* A two dimensional array. A pointer to rows of 13 integers. Incrementing this (e.g. array1++) will point
     * to the next row, which will be 13*sizeof(int) memory spaces ahead.
     * Row size 13, column size undefined. Only the rightmost array must be defined. */
    int array1[2][13]; /* Two rows, thirteen ints in each row */

    /* The array could also be initialized with values like this */
    int array2[][3] = {
            {1, 2, 4},
    };


    printf("Sizeof int: %d\n", sizeof(int));
    printf("Sizeof int array1[2][13]: %d\n", sizeof(array2));

    /* Both of these are legal */
    test_func1(array1);
    test_func2(array1);
}
