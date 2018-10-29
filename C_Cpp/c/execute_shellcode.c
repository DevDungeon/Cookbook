// https://king-sabri.net/how-to-execute-shellcode-using-ruby-on-windows-and-linux/

// Generate shellcode with something like:
// msfvenom -a x86 --platform Windows -p windows/messagebox TEXT="@KINGSABRI" -f c --smallest
char shellcode[] =
  "\xd9\xeb\x9b\xd9\x74\x24\xf4\x31\xd2\xb2\x77\x31\xc9\x64\x8b"
  "\x71\x30\x8b\x76\x0c\x8b\x76\x1c\x8b\x46\x08\x8b\x7e\x20\x8b"
  "\x36\x38\x4f\x18\x75\xf3\x59\x01\xd1\xff\xe1\x60\x8b\x6c\x24"
  "\x24\x8b";

// Windows compile
//     mingw32-gcc.exe shellcode-test.c -o shellcode-test.exe

// Linux compile
//     apt install mingw-w64
//     i686-w64-mingw32-gcc shellcode-test.c -o shellcode-test.exe -lws2_32

// int main(int argc, char **argv){int (*f)();f = (int (*)())shellcode;(int)(*f)();}
int main(int argc, char **argv)
{
  int (*func)();
  func = (int (*)()) shellcode;
  (int)(*func)();
}