#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    char c = '+';

    cout << '[' << setw(10) << c << ']' << endl;

    cout.setf(ios::left);
    cout << '[' << setw(10) << c << ']' << endl;
    cout.unsetf(ios::left);

    cout.width(4); // only applies to next thing
    cout << '[' << c << ']' << endl;


}