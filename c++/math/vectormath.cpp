#include <math.h>
#include <stdio.h>
// https://www.khanacademy.org/computing/computer-programming/programming-natural-simulations/programming-vectors/a/vector-magnitude-normalization


// Get vector magnitude (length/hypotenuse)
// a^2 + b^2 = c^2 (Pythagoras theorem for right triangles)
double vectorMagnitude(float x, float y) {
    return sqrt((x*x) + (y*y));
};


// Normalizing a vector is done by scaling it all relative to 1.
// For example, if you have the coordinates or rise/run of 3/4,
// where x(width) is 4 and the y(height) is 3. Using Pythagoras
// theorem for right triangles (shown above) is first used to get
// the magnitude of the vector (the hypotenuse of the triangle).
//    In this case, the triangle being a nice even 3/4/5 triangle.
// To scale it all, simply use the hypotenuse as the denominator.
// So the hypotenuse would be 5/5 and the others would be 3/5 and 4/5.
// The normalized vector would change from (3,4) originally, to
// (3/5, 4/5) or (0.6, 0.8).
//    You are essentially scaling down both the x and y coordinates
// individually. All you have to do is divide each of them by the
// vector magnitude.
void normalizeVector(float x, float y) {
	double magnitude = vectorMagnitude(x, y);
	float newX = x / magnitude;
	float newY = y / magnitude;
	printf("Normalization of (%f, %f): (%f, %f)\n", x, y, newX, newY);
	return;
}





int main() {
    float x = 25;
    float y = 15;
    double mag = vectorMagnitude(x, y);
    printf("Vector magnitude of (%f, %f): %f\n", x, y, mag);

	normalizeVector(3, 4);

    return 0;
}
