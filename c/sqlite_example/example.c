#include <stdio.h>
#include "sqlite3.h"

/**
 * Compile SQLite library with:
 *   gcc sqlite3.c -c -o sqlite3.o
 *
 * Compile this example app with:
 *   gcc example.c sqlite3.o -lpthread -ldl
 * or
 *   gcc example.c sqlite3.c -lpthread -ldl
 */

int main(char* argv[], int argc) {
  printf(sqlite3_libversion());
  return 0;
}
