#include <iostream>

namespace Nano {

    class File {
        public:
            static void Open() {
                std::cout << "Opening file...";
            }
    };

    class Directory {
        public:
            static void ListFiles() {
                std::cout << "test";
            }
    };

    
}

