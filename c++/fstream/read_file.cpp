// https://www.w3schools.com/cpp/cpp_files.asp
#include <iostream>
#include <fstream>
#include <string>

int main() {
	std::string myText;

	std::ifstream myfile("test.txt");
	
	if (!myfile.is_open()) {
		std::cout << "Unable to open file. Exiting." << std::endl;
		return 1;
	}

	while (getline (myfile, myText)) {
		std::cout << myText; // Print file contents
	}
	myfile.close();
}
