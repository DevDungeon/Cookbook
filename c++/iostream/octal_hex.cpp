#include <iostream>
#include <bitset>

using namespace std;

int main() {
    int x = 10;

    cout << x << endl; // print 10
    cout << oct << x << endl; // Toggle octal, print 12
    cout << hex; // Toggle hex mode
    cout << x << endl; // print a
    cout.setf(ios::uppercase); // toggle uppercase
    cout << x << endl; // print A
    cout.setf(ios::showbase); // toggle 0x prefix (0X with uppercase)
    cout << x << endl; // 0XA
    cout.unsetf(ios::uppercase);
    cout.unsetf(ios::showbase);
    cout << dec; // Restore decimal state
    cout << std::bitset<8>{42} << endl; // Output binary 0010101010
}
