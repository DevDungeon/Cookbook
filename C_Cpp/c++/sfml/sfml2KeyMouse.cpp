#include <SFML/Window.hpp>

#include <iostream>

int main() {

    std::cout << "test" << std::endl;


    sf::Window window(sf::VideoMode(800, 600), "SFML window");



    sf::Event event;
    while (window.isOpen()) {

         while (window.pollEvent(event))
        {

            if (event.type == sf::Event::Closed) {
                window.close();
            }
            else {
                std::cout << event.type << std::endl;
            }
        }

        window.setActive();
        window.display();

    }


}
