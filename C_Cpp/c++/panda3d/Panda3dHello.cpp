#include "pandaFramework.h"
#include "pandaSystem.h"

int main(int argc, char *argv[]) {
    //open a new window framework
  PandaFramework framework;
  framework.open_framework(argc, argv);
    //set the window title to My Panda3D Window
  framework.set_window_title("My Panda3D Window");
    //open the window
  WindowFramework *window = framework.open_window();

  //here is room for your own code

    //do the main loop, equal to run() in python
  framework.main_loop();
    //close the window framework
  framework.close_framework();
  return (0);
}
