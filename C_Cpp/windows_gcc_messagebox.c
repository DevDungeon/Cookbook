// Can be compiled with gcc on Windows (MinGW)
// gcc windows_gcc_messagebox.c
// MinGW comes with it's own windows.h header
// Make sure the MinGW\bin dir is in the PATH so it can find all the .dll files needed

// http://winprog.org/tutorial/start.html

#include <windows.h>

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, 
    LPSTR lpCmdLine, int nCmdShow)
{
    MessageBox(NULL, "Goodbye, cruel world!", "Note", MB_OK);
    return 0;
}