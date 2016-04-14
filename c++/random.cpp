#include <time.h>
#include <stdlib.h>
#include <iostream>

int main(int argc, char **argv) {
	srand(time(0));
	std::cout << rand() << std::endl;
	return(0);
}
