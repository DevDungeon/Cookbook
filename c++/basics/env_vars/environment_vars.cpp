#include <iostream>
#include <cstdlib>

int main() {
	const char* env;
	env = std::getenv("PATH");

	if (env) {
		std::cout << "PATH: " << env << std::endl;
	}
}
