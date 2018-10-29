#include <iostream>

using namespace std;

int main() {
    char c = 'x';

    // endl flushes the buffer, outputting data to screen. Otherwise it buffers and waits
    cout << c << endl;
    cout << flush; // You can manually flush this way too

    cout.put(c);
    cout.put('\n'); // This does not flush the buffer
    cout.flush(); // Force flush manually

    // cerr flushes automatically after every insert
    cerr << c;
}