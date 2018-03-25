#include <iostream>
#include <nanofile.h>

int main() {

    std::cout << "Testing the NanoFile library..." << std::endl;
    Nano::File::Open();
    Nano::Directory::ListFiles();
}