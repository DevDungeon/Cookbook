#ifndef CLEANUP_HPP_INCLUDED
#define CLEANUP_HPP_INCLUDED

void cleanup() {

    glfwCloseWindow();
    glfwTerminate();

}


#endif // CLEANUP_HPP_INCLUDED
