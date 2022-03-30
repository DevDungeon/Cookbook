// Modified from: https://www.cplusplus.com/reference/cstdlib/rand/
#include <stdio.h>     // printf, scanf, puts, NULL
#include <stdlib.h>    // srand, rand
//#include <time.h>      // time
#include <sys/time.h>  // gettimeofday, struct timeval

int main() {

	// Seed - option 1: time()
	// time() is only updated every second. Option 2 better
	// srand (time(NULL)); // #include <time.h>
	// With time(), if you run this program multiple times
	// in the same second,
	// The random numbers will be the same since time() will only
	// return a different value after a second has elapsed.

	// Seed - option 2: high resolution time with timeval
	// This lets you run the program many times per second and still
	// get different random seeds.
	struct timeval currentTime;
	gettimeofday(&currentTime, 0);
	printf("%d\n", currentTime.tv_usec);
	srand(currentTime.tv_usec);


	printf("Maximum random number: %d\n", RAND_MAX);

	int randomNum = rand();
	printf("Random: %d\n", randomNum);

	int limitedNum = (randomNum % 10) + 1;
	printf("Random 1-10: %d\n", limitedNum);

	return 0;
}

