#include <cstdlib>
#include <iostream>

int main() {
    // Run external programs with system()
    system("ls");
    system("echo $HOME"); // Env vars are inherited
    system("pwd");
    int return_value = system("zenity --calendar");
    std::cout << return_value << std::endl; // 0 is good
    system("man man");

}
