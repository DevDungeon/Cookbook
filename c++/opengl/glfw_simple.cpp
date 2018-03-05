// Compile with: g++ -lglfw
#include <GLFW/glfw3.h>
#include <iostream>
//sudo apt-get install libglfw3
//sudo apt-get install libglfw3-dev
// and maybe libglu1-mesa-dev freeglut3-dev libglew1.5 libglew1.5-dev libglu1-mesa libglu1-mesa-dev libgl1-mesa-glx libgl1-mesa-dev
// Windows NuGet command:  Install-Package nupengl.core 



int main(int argc, char** argv)
{
    if (glfwInit() == false) {
        std::cerr << "GLFW failed to initialize." << std::endl;
        return -1;
    }
    return 0;
}