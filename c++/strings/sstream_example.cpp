// stringstream
#include <iostream>
#include <sstream>
#include <iomanip> // for setw

using namespace std;

int main() {

	stringstream my_stream;

	my_stream << "Hello" << endl;
	my_stream.setf(ios::showbase);
	my_stream << hex << 128 << endl;
	my_stream.unsetf(ios::showbase);
	my_stream << setw(10) << "hi" << setw(10) << "hi" << endl;
	cout << my_stream.str();
	cout << my_stream.str().c_str();
	// Reset stream
	my_stream.clear(); // clear flags
	my_stream.str(""); // Set it to empty string
	

}
