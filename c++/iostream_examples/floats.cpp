#include <iostream>

using namespace std;

int main() {
    float f = 6.5;

    cout << f << endl;

    cout.setf(ios::showpoint);
    cout << f << endl;
    cout.unsetf(ios::showpoint);

    cout.setf(ios::scientific);
    cout << f << endl;

    cout.setf(ios::uppercase);
    cout.precision(3);
    cout << f << endl;
    cout.unsetf(ios::uppercase);
    cout.unsetf(ios::scientific);

    cout.precision(3);
    cout << f << endl;


}