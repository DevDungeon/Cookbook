// gcc print_ascii_in_binary.cpp -lstdc++
#include <iostream>

// Take the input and print out ASCII characters. Useful for finding strings
// in binary files.
int main(int argc, char* argv[]) {
    bool last_char_was_whitespace = false;
    char c;

    while (std::cin.get(c)) {
        if (
               (c >= 'a' && c <= 'z') 
            || (c >= '0' && c <= '9')
            || (c >= 'A' && c <= 'Z')
        ) {
            std::cout << c;
            last_char_was_whitespace = false;
        } else if (c == '\n' || c == '\t' || c== ' ' && !last_char_was_whitespace) {
            last_char_was_whitespace = true;
            std::cout << " ";
        }
    }
    
    // fstream f;
    // f = myfile.open("file.dat", ios::out | ios::in );
    // f.get(c)

	return 0;
}

