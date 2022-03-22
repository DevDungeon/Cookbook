#include <SFML/Window.hpp>
#include <SFML/Graphics.hpp>
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
			// Window events
			case sf::Event::Closed:
				window->close();
				break;
			//sf::Event::Resized
			//sf::Event::LostFocus sf::Event::GainedFocus
			
			case sf::Event::KeyPressed:
				text.setString("Key pressed");
				break;
			case sf::Event::KeyReleased:
				text.setString("Key released");
				break;
			
			// Mouse events
			case sf::Event::MouseButtonPressed:
				text.setString("Mouse button pressed");
				break;
			case sf::Event::MouseWheelScrolled:
				text.setString("Mouse wheel scrolled");
				break;
			//sf::Event::MouseMoved
			//sf::Event::MouseEntered sf::Event::MouseLeft
			
			// Joystick events
			
			//sf::Event::JoystickButtonPressed sf::Event::JoystickButtonReleased
			//sf::Event::JoystickMoved
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
	text.rotate(0.1f);
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
