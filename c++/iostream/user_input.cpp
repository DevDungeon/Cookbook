#include <iostream>
#include <limits>

using std::cout; using std::endl; using std::cin;

int main() {
	int numPlayers = 0;
	cout << "Enter a number 1-8: ";
	while (!(cin >> numPlayers)) {
		cout << "Sorry, I did not understand that number. Try again." << endl;
		cout << "Enter a number 1-8: ";
		cin.clear();
		cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
	}
	cout << "You chose " << numPlayers << " players." << endl;
	if (numPlayers < 1 || numPlayers > 8)
		cout << "But you didn't follow directions." << endl;
}
