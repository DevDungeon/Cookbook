#include <stdio.h>
#include <stdint.h>
/**

printf is a program you can run too. Reference: `man printf`

For C function reference, use man page 3: `man 3 printf`

There is also printf to output to different places:

To STDOUT (fd 1) `man stdout`
  int printf(const char *format, ...);

To a file desriptor like 1, 2 (stderr)
  int dprintf(int fd, const char *format, ...);

To a FILE pointer
  int fprintf(FILE *stream, const char *format, ...);

To a buffer without size limit
  int sprintf(char *str, const char *format, ...);

To a buffer with a maximum limit on size
  int snprintf(char *str, size_t size, const char *format, ...);




## Placeholder symbols
 
Reference from https://www.cplusplus.com/reference/cstdio/printf/

symbol	Output				Example
d	int						392
u	Unsigned int			7235
o	octal					610
x	hex (lower(				7fa
X	hex (upper)				7FA
f	float					392.65


e	Scientific exponent lowercase	3.9265e+2
E	Scientific exponent uppercase	3.9265E+2
g	Use shortest of %e or %f		392.65
G	Use shortest of %E or %F		392.65

c	Character				a
s	String of characters
p	Pointer address			0x557f3f1a911d

%	A % followed by another % character will write a single % to the stream
*/
// Helper function for printing binary
void printBits(unsigned char byte);
void printBytes(size_t const numBytes, void const * const ptr);

int main(int argc, char* argv[]) {
	// Basic printf
	printf("Hello, world!\n");
	puts("puts outputs a string w/o formatting & includes newline.");
	

	// ints
	printf("int (dec): %d \n", 100); //unsigned: %u
	printf("int (oct): %o %#o \n", 100, 100); // without, with 0 prefix
	printf("int (hex): %x, %X, %#x, %#X \n", 100, 100, 100, 100); // lower, upper, 0x prefixed
	
	// set width/precede with blanks or zeroes
	printf("int with preceeding space: %15d \n", 100); // works with other types too
	printf("char with preceeding space: %15c \n", 'x'); // works with other types too
	printf("variable width: %*c \n", 15, 'x');

	// floats
	printf("float: %f\n", 2.51);
	printf("float (scientific): %e \n", -142000000000.0);

	// char and string
	char* text = "Hello, this is my text!";	
	printf("char: %c and string: %s \n", 'x', text);
	
	// binary
	uint16_t n;
	n = 1;
	printBytes(sizeof(n), &n);
	n = 127;
	printBytes(sizeof(n), &n);
	n = 255;
	printBytes(sizeof(n), &n);
	n = 65535;
	printBytes(sizeof(n), &n);

	// pointer address
	printf("Pointer address for `char* text`: %p \n", text);
	
	// Escape the percent sign to print a literal %
	printf("You can print a %% this way.\n");
	

	
	

}


void printBits(unsigned char byte) {
	for (int j = 7; j >= 0; j--) {      // For each bit in the byte
		printf("%u", (byte >> j) & 1);  // Print the 1 or 0
	}
}

//                                Pointer to the object
// How many bytes the object is                       |
//                           |                        |
void printBytes(size_t const numBytes, void const * const ptr)
{
	// Prints any kind of object
	// Assumes little endian like intel
	// Reference: https://stackoverflow.com/questions/111928/is-there-a-printf-converter-to-print-in-binary-format
    unsigned char *buffer = (unsigned char*) ptr;
    unsigned char tempByte;
    
    for (int i = numBytes-1; i >= 0; i--) {          // For each byte provided
		printBits(buffer[i]);
    }
    puts(""); // print a newline
}

