#include <iostream>

#include <GL/glew.h>    // also includes gl.h
#include <GL/glfw.h>
#include <glm/glm.hpp>  // header only
//link to: glew32, glfw, opengl32, glu32

int main() {

    int running = GL_TRUE;

    //GLFW Init
    glfwInit();

    //glfwOpenWindowHint(GLFW_OPENGL_VERSION_MAJOR, 4);         //use these for version 3+
    //glfwOpenWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
    if( !glfwOpenWindow( 300,300, 0,0,0,0,0,0, GLFW_WINDOW ) ) {
        glfwTerminate();
        std::cout << "Error opening GLFW window" << std::endl;
        exit( EXIT_FAILURE );
    }
    glfwSetWindowTitle("Window Title");
    glfwSetWindowSize(1024, 768);
    glfwSetWindowPos(0, 0);
    // END GLFW INIT

    // GLEW INIT
    GLenum err = glewInit(); // glew init requires an active context
    if (GLEW_OK != err) {
       std::cout << "Glew error: " << glewGetErrorString(err) << std::endl;
    } else {
        std::cout << "Glew version: " << glewGetString(GLEW_VERSION) << std::endl;
    }
    // END GLEW INIT




    gluPerspective(90.f, 1.f, 1.f, 500.f); // fovy, aspect, zNear, zFar
    glTranslatef(120.f, 120.f, -300.f);



    // Main Loop
    while ( running ) {


        gluPerspective(90.f, 1.f, 1.f, 500.f);



        glClear( GL_COLOR_BUFFER_BIT );

        glBegin(GL_QUADS);

            glVertex3f(-50.f, 0, -50.f);
            glVertex3f(-50.f, 0, -50.f);
            glVertex3f( 50.f,  0, -50.f);
            glVertex3f( 50.f, 0, -50.f);

            glVertex3f(-50.f, -50.f, 50.f);
            glVertex3f(0,  0, 50.f);
            glVertex3f( 50.f,  50.f, 50.f);
            glVertex3f( 50.f, -50.f, 50.f);

            glVertex3f(-50.f, -50.f, -50.f);
            glVertex3f(0,  50.f, -50.f);
            glVertex3f(-50.f,  50.f,  50.f);
            glVertex3f(-50.f, -50.f,  50.f);

            glVertex3f(50.f, -50.f, -50.f);
            glVertex3f(50.f,  50.f, 0);
            glVertex3f(50.f,  50.f,  50.f);
            glVertex3f(50.f, -50.f,  50.f);

            glVertex3f(-50.f, -50.f,  50.f);
            glVertex3f(-50.f, -50.f, -50.f);
            glVertex3f( 50.f, -50.f, -50.f);
            glVertex3f( 50.f, -50.f,  50.f);

            glVertex3f(-50.f, 50.f,  50.f);
            glVertex3f(-50.f, 50.f, -50.f);
            glVertex3f( 50.f, 50.f, -50.f);
            glVertex3f( 50.f, 50.f,  50.f);

        glEnd();

        glfwSwapBuffers();

        running = !glfwGetKey( GLFW_KEY_ESC ) && glfwGetWindowParam( GLFW_OPENED );

    }




    // Clean up
    glfwTerminate();
    return ( EXIT_SUCCESS );

}
