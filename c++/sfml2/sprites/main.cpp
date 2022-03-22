// https://www.sfml-dev.org/tutorials/2.5/graphics-sprite.php
#include <SFML/Window.hpp>
#include <SFML/Graphics.hpp>

 int main() {
     
     sf::RenderWindow window(sf::VideoMode(800, 600), "Sprites Example");
     window.setFramerateLimit(60);
     
     
	 // Load image
	 sf::Texture texture;
	if (!texture.loadFromFile("sprite.png"))
	{
		// error...
		puts("Error loading image.");
		return(1);
	}
	
	// or 
	// only load a 32x32 rectangle that starts at (10, 10)
	//texture.loadFromFile("image.png", sf::IntRect(10, 10, 32, 32)))
	// or
    // create an empty 200x200 texture
	//texture.create(200, 200))
	 sf::Sprite sprite;
	 
	sprite.setTexture(texture);
	 
	 
	 
	// position
	//sprite.setPosition(sf::Vector2f(10.f, 50.f)); // absolute position
	//sprite.move(sf::Vector2f(5.f, 10.f)); // offset relative to the current position

	// rotation
	//sprite.setRotation(90.f); // absolute angle
	//sprite.rotate(15.f); // offset relative to the current angle

	// scale
	//sprite.setScale(sf::Vector2f(0.5f, 2.f)); // absolute scale factor
	//sprite.scale(sf::Vector2f(1.5f, 3.f)); // factor relative to the current scale
	 


     
     while (window.isOpen()) {
        
        // Event processing
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed) window.close();
            if (event.type == sf::Event::KeyPressed) {
				sprite.rotate(15.f); // Relative rotate
				sprite.move(sf::Vector2f(5.f, 10.f));
			}
        }
        
        // Add sprite
        window.clear();
		window.draw(sprite);
        
        window.setActive();
        // OpenGL drawing commands go here...
        window.display();
     }

 }
