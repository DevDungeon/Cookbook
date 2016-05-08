#include <iostream>

using namespace std;

int main() {
    int x = 10;

    cout << x << endl;
    cout << oct << x << endl;

    cout << hex;
    cout << x << endl;
    cout.setf(ios::uppercase);
    cout << x << endl;
    cout.setf(ios::showbase);
    cout << x << endl;
    cout.unsetf(ios::uppercase);
    cout.unsetf(ios::showbase);

    cout << dec; // Restore decimal state
}