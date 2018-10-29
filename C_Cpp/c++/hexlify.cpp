/**
 * hexlify.cpp
 * 
 * gcc hexlify.cpp -lstdc++
 * 
 * Output the contents of STDIN as hexidecimal
 */
#include <iostream>
#include <iomanip>

int main(int argc, char** argv) {
    char c;
    int hexGroupCount = 0;
    int columnSize = 2; // Number of hex digits grouped
    int columnCount = 0;
    int numColumns = 8;

    while (std::cin.get(c)) {

        // Print out hex content
        std::cout << std::hex
            << std::setfill('0') 
            << std::uppercase
            //<< std::setw(8) // for binaries?
            << std::setw(2) // For ASCII files
            << int(c);
        hexGroupCount++;

        // Break in to groups/newlines
        if (hexGroupCount >= columnSize) {
            if (columnCount >= numColumns) {
                std::cout << std::endl;
                columnCount = 0;
                hexGroupCount = 0;
                continue;
            }
            std::cout << " ";
            hexGroupCount = 0;
            columnCount++;
        }
    }
}