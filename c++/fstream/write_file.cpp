#include <iostream>
#include <fstream>


int main() {
  
	std::ofstream myfile("test.txt");
	if (!myfile.is_open()) {
		std::cout << "Unable to open file. Exiting." << std::endl;
		return 1;
	}
	myfile << "Writing text to file.\nHello, world!\nBye.";
	myfile.close();

	// Write binary file
	std::ofstream mybinfile("test.bin");
	if (!mybinfile.is_open()) {
		std::cout << "Unable to open file. Exiting." << std::endl;
		return 1;
	}
	
	char* x = "Hello, world!\n";
	mybinfile.write((char*)&x, sizeof(x));
	mybinfile.close();

    
  
} 
