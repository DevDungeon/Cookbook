/**
 * Tested with XBox 360 Controller connected over USB
 * 
 * Joystick ID will refer to individual controllers.
 * One controller with have two physical joysticks (4 technically,
 * because the triggers are pressure sensitive and act like joysticks).
 * The triggers only go from 0-100 whereas the others go -100 to 100.
 * 
 * Buttons:
 * 
 * a b x y, (0, 1, 2, 3)
 * l1 r1
 * select start logo
 * left joystick press, right joystick press
 * 
 * Joystick Axes:
 * 
 * left joystick= 0, 1 (sf::Joystick::X, sf::Joystick::Y)
 * left trigger = 2 (sf::Joystick::Z)
 * right trigger = 3 (sf::Joystick::R) 
 * right joystick = 4, 5 (sf::Joystick::U, sf::Joystick::V)
 *
 * Arrow pad:
 * PovX and PovY (-100 on up/left, 100 on right/down)
 
 * 
 */
#include <SFML/Window.hpp>
#include <SFML/Graphics.hpp>
#include <iostream>
//#include <SFML/Audio.hpp>
//#include <SFML/Network.hpp>

sf::RenderWindow* window;

sf::Font defaultFont;
sf::Text leftJoyXText, leftJoyYText;

sf::Texture texture;



void processEvents(sf::RenderWindow* window) {
	// Event processing https://www.sfml-dev.org/tutorials/2.5/window-events.php
	sf::Event event;
	while (window->pollEvent(event))	{
		switch (event.type) {
			
			// Joystick events
			case sf::Event::JoystickConnected:
				//std::cout << "joystick connected: " << event.joystickConnect.joystickId << std::endl;
				break;
			case sf::Event::JoystickDisconnected:
				//std::cout << "joystick disconnected: " << event.joystickConnect.joystickId << std::endl;
				break;
			case sf::Event::JoystickButtonPressed:
				if (event.type == sf::Event::JoystickButtonPressed)
				{
					//std::cout << "joystick button pressed!" << std::endl;
					//std::cout << "joystick id: " << event.joystickButton.joystickId << std::endl;
					//std::cout << "button: " << event.joystickButton.button << std::endl;
				}
				break;
			case sf::Event::JoystickButtonReleased:
					std::cout << "Joystick button released." << std:: endl;
				break;
			case sf::Event::JoystickMoved:
				switch(event.joystickMove.axis) {
				
				case sf::Joystick::X:
				
					leftJoyXText.setString(std::to_string(event.joystickMove.position));
					break;
				
				case sf::Joystick::Y:

					leftJoyYText.setString(std::to_string(event.joystickMove.position));
					break;
					
				case sf::Joystick::Z:
					// Left trigger
					break;
				
				case sf::Joystick::R:
					// Right trigger
					// Set bar to {-100-100)
					break;

				else if (event.joystickMove.axis == sf::Joystick::U ||
						event.joystickMove.axis == sf::Joystick::V)
				{
					std::cout << "Right joystick moved" << std::endl;
				}
				else if (event.joystickMove.axis == sf::Joystick::PovX)
				{
					if (event.joystickMove.position == -100) // Left arrow
					{
						
					}
					else if (event.joystickMove.position == 100) // Down arrow
					{
					}
				}
				else if (event.joystickMove.axis == sf::Joystick::PovY)
				{
					if (event.joystickMove.position == -100) // Up arrow
					{
					}
					else if (event.joystickMove.position == 100) // Down arrow
					{
					}
					
					
					
					
				}

				
			
				break;
				

			case sf::Event::Closed:
				window->close();
				break;
			case sf::Event::Resized:
				break;
			case sf::Event::LostFocus:
				break;
			case sf::Event::GainedFocus:
				break;
			
			// Keyboard events
			case sf::Event::KeyPressed:
				std::cout << "Keyboard press. " << std::endl;
				break;
			case sf::Event::KeyReleased:
				break;
			
			// Mouse events
			case sf::Event::MouseButtonPressed:
				break;
			case sf::Event::MouseWheelScrolled:
				break;
			case sf::Event::MouseMoved:
				break;
			
			default:
				std::cout << "Unknown event " << std::endl;
				break;
		}
	}
}

void drawFrame(sf::RenderWindow* window) {
	window->clear();
	
	// TODO Draw the baselayer (the UI frame for each element)
	// Draw circles to encompass the joysticks
	// Draw boxes to encompass the trigger presses
	// Draw circles that act like buttons and light up when pressed
	// Draw the outline/sprite that looks like an xbox controller
	
	// Draw each dynamic element (the slider/joystick values/etc)
	window->draw(leftJoyXText);
	window->draw(leftJoyYText);
}


void setup(sf::RenderWindow* window) {
	
	defaultFont.loadFromFile("/home/odin/Cookbook/c++/sfml2/template/OCR-A.ttf");
	
	
	
	leftJoyXText.setFont(defaultFont);
	leftJoyYText.setFont(defaultFont);
	leftJoyXText.setString("Left Joystick X");
	leftJoyYText.setString("Left Joystick Y");
	
	
	leftJoyXText.setCharacterSize(40); // in pixels, not points!
	leftJoyYText.setCharacterSize(40); // in pixels, not points!
	leftJoyXText.setFillColor(sf::Color::Cyan);
	leftJoyYText.setFillColor(sf::Color::Cyan);
	
	leftJoyXText.move(50, 50);
	leftJoyXText.move(80, 50);
	
	
	window->setFramerateLimit(60);
	window->setActive();
	std::cerr << "Done setting up." << std::endl;
}

int main(int argc, char* argv[]) {
	window = new sf::RenderWindow(sf::VideoMode(800, 600), "My app");

	setup(window);

	while (window->isOpen()) {
		processEvents(window);
		
		drawFrame(window);
		window->display();
	}

}
