#include <iostream>
#include <bitset>
#include <string>

int main() {
	std::cout << std::bitset<16>(255) << std:: endl;
	
	uint16_t i = 65534;
	std::string s1 = std::bitset<8 * sizeof(i)>(i).to_string();
	std::cout << s1 << std::endl;
	
	int32_t n = 25;
	std::string s2 = std::bitset<8 * sizeof(n)>(n).to_string();
	std::cout << s2 << std::endl;
	
	n = -25;
	std::string s3 = std::bitset<8 * sizeof(n)>(n).to_string();
	std::cout << s3 << std::endl;
}
