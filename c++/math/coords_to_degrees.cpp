#include <math.h>
#include <iostream>

/**
 * Given (x,y) coordinates, convert to radians then degrees
 */
float xy_to_degrees(int x, int y) {
	float radians = atan2(y, x); // math.h
	float degrees = radians * (180/M_PI);
	// 0 degrees will be north, 90=east,-90=west,180=south
	return degrees;
}




int main() {

	// To convert between x,y coordinates and degrees,
	// you can use atan2(x,y) to get radians, then convert to degrees.

	int x,y;
/*
	std::cout << "Please provide an x coordinate: ";
	std::cin >> x;
	std::cout << "Please provide a y coordinate: ";
	std::cin >> y;
*/

int xs[4] = {1000, 0, -1000, 0};
int ys[4] = {0, 1000, 0, -1000};
for (int i = 0; i < 4; i++) {
	x = xs[i];
	y = ys[i];

	std::cout << "========================" << std::endl;
	std::cout << "Received coordinates: (" << x << "," << y << ")" << std::endl;

	std::cout << "[*] Converting to radians..." << std::endl;
	float angleInRadians = atan2(x, y);
	std::cout << "in radians: " << angleInRadians << std::endl;
	
	std::cout << "[*] Converting to degrees..." << std::endl;
	float degrees = angleInRadians * (180/M_PI);
	std::cout << "Degrees: " << degrees << std::endl;
}
}
