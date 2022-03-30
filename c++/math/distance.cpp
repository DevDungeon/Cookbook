// From: https://www.geeksforgeeks.org/program-calculate-distance-two-points/
#include <stdio.h>
#include <bits/stdc++.h> // std::sqrt(), std::pow()


// Function to calculate distance between two points
float distance(int x1, int y1, int x2, int y2)
{
    return std::sqrt(std::pow(x2 - x1, 2) +
                std::pow(y2 - y1, 2) * 1.0);
}

int main() {
	int x1 = 10;
	int y1 = 10;
	int x2 = 20;
	int y2 = 25;
	float dist = distance(x1, y1, x2, y2);

	printf("The distance between (%d,%d) and (%d,%d) is %f\n.", x1, y1, x2, y2, dist);
	return 0;
}
