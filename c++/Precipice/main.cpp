#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <glload/gl_3_3_comp.h>
#include <glload/gll.hpp> // OpenGL function loader
#include <GL/glfw.h> // Window/Input/Timing

#include "vertices.hpp"
#include "init.hpp"
#include "cleanup.hpp"
#include "display.hpp"

int main() {

    int running = GL_TRUE;

    init();

    while( running )        // Main loop
    {

        // Poll input
        running = !glfwGetKey( GLFW_KEY_ESC ) && glfwGetWindowParam( GLFW_OPENED );

        // Handle actions
        //move_stuff() and calculate()

        // Render display
        //display();
        //test_display();
        //moveByMouse();
        orthoCubedisplay();

    }

    cleanup();

    return 0;

}
