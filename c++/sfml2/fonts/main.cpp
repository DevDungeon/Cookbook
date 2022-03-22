// https://wwwsfml-dev.org/tutorials/2.5/graphics-text.php
// https://www.sfml-dev.org/documentation/2.5.1/classsf_1_1Text.php
#include <SFML/Window.hpp>
#include <SFML/Graphics.hpp>

 int main() {
	sf::Font font;
	if (!font.loadFromFile("OCR-A.ttf"))
	{
		// error...
	}
	
	sf::Text text;
	text.setFont(font); // font is a sf::Font
	text.setString("Hello world");
	text.setCharacterSize(24); // in pixels, not points!
	text.setFillColor(sf::Color::Cyan);
	text.setStyle(sf::Text::Bold | sf::Text::Underlined);

     
	 
	 
     sf::RenderWindow window(sf::VideoMode(800, 600), "SFML window");
     window.setFramerateLimit(60);
     
     

     
     while (window.isOpen())
     {
        // Event processing
        sf::Event event;
        while (window.pollEvent(event))
        {
            // Request for closing the window
            if (event.type == sf::Event::Closed)
                window.close();
        }

		window.clear();
        window.setActive();
        
        text.rotate(0.1f);
        window.draw(text);

        window.display();
     }

 }
