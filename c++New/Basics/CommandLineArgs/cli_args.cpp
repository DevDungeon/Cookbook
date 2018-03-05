#include <iostream>

int main(int num_args, char** args) {
	std::cout << "Args entered:" << std::endl;
	for (int i = 0; i < num_args; i++) {
		std::cout << args[i] << " ";
	}
	std::cout << std::endl;
	return 0;
}
