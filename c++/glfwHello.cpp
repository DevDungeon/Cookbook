#include <iostream>

#include <GL/glew.h>    // also includes gl.h
#include <GL/glfw.h>
#include <glm/glm.hpp>  // header only
//link to: glew32, glfw, opengl32, (glu32??)

int main() {

    int running = GL_TRUE;

    //GLFW Init
    glfwInit();
    if( !glfwOpenWindow( 300,300, 0,0,0,0,0,0, GLFW_WINDOW ) ) {
        glfwTerminate();
        exit( EXIT_FAILURE );
    }
    // END GLFW INIT

    // GLEW INIT
    GLenum err = glewInit(); // glew init requires an active context
    if (GLEW_OK != err) {
       std::cout << "Glew error: " << glewGetErrorString(err) << std::endl;
    } else {
        std::cout << "Glew version: " << glewGetString(GLEW_VERSION) << std::endl;
    }
    // END GLEW INIT


    // Main Loop
    while ( running ) {

        glClear( GL_COLOR_BUFFER_BIT );

        glfwSwapBuffers();

        running = !glfwGetKey( GLFW_KEY_ESC ) && glfwGetWindowParam( GLFW_OPENED );

    }




    // Clean up
    glfwTerminate();
    return 0;

}
