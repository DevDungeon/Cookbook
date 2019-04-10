#include <stdio.h>

// Compile with: gcc test.c mylib.o

int main(int argc, char **argv) {
    extern multiply(int, int);
    int product = multiply(6, 4);
    printf("Product: %d.\n", product);
    return 0;
}