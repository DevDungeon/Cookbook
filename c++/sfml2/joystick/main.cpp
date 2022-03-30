#include <SFML/Window.hpp>
#include <SFML/Graphics.hpp>
#include <iostream>
//#include <SFML/Audio.hpp>
//#include <SFML/Network.hpp>

sf::RenderWindow* window;

sf::Font font;
sf::Text text;

sf::Texture texture;
sf::Sprite sprite;



void processEvents(sf::RenderWindow* window) {
	// Event processing https://www.sfml-dev.org/tutorials/2.5/window-events.php
	sf::Event event;
	while (window->pollEvent(event))	{
		switch (event.type) {
			
			// Joystick events
			case sf::Event::JoystickConnected:
				std::cout << "joystick connected: " << event.joystickConnect.joystickId << std::endl;
				break;
			case sf::Event::JoystickDisconnected:
				std::cout << "joystick disconnected: " << event.joystickConnect.joystickId << std::endl;
				break;
			case sf::Event::JoystickButtonPressed:
					std::cout << "joystick button pressed!" << std::endl;
					std::cout << "joystick id: " << event.joystickButton.joystickId << std::endl;
					std::cout << "button: " << event.joystickButton.button << std::endl;
				break;
			case sf::Event::JoystickButtonReleased:
					std::cout << "Joystick button released." << std:: endl;
				break;
			case sf::Event::JoystickMoved:
				if (event.joystickMove.axis == sf::Joystick::X ||
					event.joystickMove.axis == sf::Joystick::Y)
				{
					std::cout << "Left joystick moved." << std::endl;
				}
				else if (event.joystickMove.axis == sf::Joystick::Z)
				{
					std::cout << "Left trigger pressed." << std::endl;
				}
				else if (event.joystickMove.axis == sf::Joystick::R) {
					std::cout << "Right trigger pressed." << std::endl;
				}
				else if (event.joystickMove.axis == sf::Joystick::U ||
						event.joystickMove.axis == sf::Joystick::V)
				{
					std::cout << "Right joystick moved" << std::endl;
				}

				
				std::cout << event.joystickMove.axis << " axis moved!" << std::endl; // https://www.sfml-dev.org/documentation/2.5.1/structsf_1_1Event_1_1JoystickMoveEvent.php
				std::cout << "joystick id: " << event.joystickMove.joystickId << std::endl;
				std::cout << "new position: " << event.joystickMove.position << std::endl;
			
				break;
				/**
				 * https://www.sfml-dev.org/documentation/2.5.1/classsf_1_1Joystick.php#a48db337092c2e263774f94de6d50baa7
				 * 
				 * With an XBOX 360 controller, XY axes are the left joystick.
				 * UV axes are the second joystick
				 * ZR are the triggers with pressure sensitivity
				 * Axes supported by SFML joysticks.
Joystick axes for the xbox360 controller
left joystick= 0, 1 (sf::Joystick::X, sf::Joystick::Y)
left trigger = 2 (sf::Joystick::Z)
right trigger = 3 (sf::Joystick::R) 
right joystick = 4, 5 (sf::Joystick::U, sf::Joystick::V)
There is also the arrow key pad:
PovX 	The X axis of the point-of-view hat.
PovY 	The Y axis of the point-of-view hat. 
				 * 
				 * 
				 */

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
				std::cout << "Unknown event " << event.type << std::endl;
		}
	}
}

void drawFrame(sf::RenderWindow* window) {
	window->clear();

	window->draw(sprite);
	window->draw(text);

	window->display();
}


void updateState() {
	sprite.rotate(0.1f);
}

void setup(sf::RenderWindow* window) {
	if (!texture.loadFromFile("sprite.png")) { /* Error */ }
	if (!font.loadFromFile("OCR-A.ttf")){ /* Error */ }
	
	sprite.setTexture(texture);
	
	text.setFont(font);
	text.setString("Hello world");
	text.setCharacterSize(24); // in pixels, not points!
	text.setFillColor(sf::Color::Cyan);
	text.setStyle(sf::Text::Bold | sf::Text::Underlined);
	text.move(window->getSize().x / 2, window->getSize().y/2);
	
	window->setFramerateLimit(60);
	window->setActive();
}

int main(int argc, char* argv[]) {
	window = new sf::RenderWindow(sf::VideoMode(800, 600), "My app");

	setup(window);

	while (window->isOpen()) {
		processEvents(window);
		updateState();
		drawFrame(window);
	}

}
