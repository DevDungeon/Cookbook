// g++ -c main.cpp
// g++ -c main.cpp -I<sfml-install-path>/include

// g++ main.o -o sfml-app -lsfml-graphics -lsfml-window -lsfml-system
// g++ main.o -o sfml-app -L<sfml-install-path>/lib -lsfml-graphics -lsfml-window -lsfml-system
#include <SFML/Window.hpp>
#include <iostream>

 int main() {
	 sf::Window window(sf::VideoMode(800, 600), "SFML window");
	 window.setFramerateLimit(60);
	 


     while (window.isOpen()) {
		 
		 // Check if a key is pressed at any moment
		 if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left)) { std::cout<<"Left" << std::endl; }
		 if (sf::Mouse::isButtonPressed(sf::Mouse::Left)) { std::cout<<"LMB"<< std::endl; }
		 
		 // get the global mouse position (relative to the desktop)
		sf::Vector2i globalPosition = sf::Mouse::getPosition();

		// get the local mouse position (relative to a window)
		sf::Vector2i localPosition = sf::Mouse::getPosition(window); // window is a sf::Window

		
		 // set the mouse position globally (relative to the desktop)
		//sf::Mouse::setPosition(sf::Vector2i(500, 100));
		// set the mouse position locally (relative to a window)
		//sf::Mouse::setPosition(sf::Vector2i(10, 50), window); // window is a sf::Window
		 
		// Event handling
        sf::Event event;
        while (window.pollEvent(event)) {
			
			
			
			
			switch (event.type) {
				case sf::Event::Closed:
					window.close();
					break;
				case sf::Event::KeyPressed:
					break;
				default:
					break;
			}
            if (event.type == sf::Event::Closed) window.close();
            
        }

        // Activate the window for OpenGL rendering
        window.setActive();

        // OpenGL drawing commands go here...

        // End the current frame and display its contents on screen
        window.display();
     }

 }
 
 /*
 
 

sf::Event::KeyPressed
if (event.key.code == sf::Keyboard::Escape)
    {
        std::cout << "the escape key was pressed" << std::endl;
        std::cout << "control:" << event.key.control << std::endl;
        std::cout << "alt:" << event.key.alt << std::endl;
        std::cout << "shift:" << event.key.shift << std::endl;
        std::cout << "system:" << event.key.system << std::endl;
    }
sf::Event::KeyReleased
sf::Event::GainedFocus
sf::Event::LostFocus
sf::Event::TextEntered
sf::Event::Resized)
{
    std::cout << "new width: " << event.size.width << std::endl;
    std::cout << "new height: " << event.size.height << std::endl;
}

if (event.type == sf::Event::MouseWheelScrolled)
{
    if (event.mouseWheelScroll.wheel == sf::Mouse::VerticalWheel)
        std::cout << "wheel type: vertical" << std::endl;
    else if (event.mouseWheelScroll.wheel == sf::Mouse::HorizontalWheel)
        std::cout << "wheel type: horizontal" << std::endl;
    else
        std::cout << "wheel type: unknown" << std::endl;
    std::cout << "wheel movement: " << event.mouseWheelScroll.delta << std::endl;
    std::cout << "mouse x: " << event.mouseWheelScroll.x << std::endl;
    std::cout << "mouse y: " << event.mouseWheelScroll.y << std::endl;
}

if (event.type == sf::Event::MouseMoved)
{
    std::cout << "new mouse x: " << event.mouseMove.x << std::endl;
    std::cout << "new mouse y: " << event.mouseMove.y << std::endl;
}

if (event.type == sf::Event::MouseEntered)
    std::cout << "the mouse cursor has entered the window" << std::endl;

if (event.type == sf::Event::MouseLeft)
    std::cout << "the mouse cursor has left the window" << std::endl;
    
    
    */
