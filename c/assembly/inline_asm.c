/**

For inline assembly, use __asm__() or asm();

Reference:
https://www.codeproject.com/Articles/15971/Using-Inline-Assembly-in-C-C

asm ( "assembly code"
   : output operands             // optional 
   : input operands              // optional 
   : list of clobbered registers // optional 
);

*/
#include <stdio.h>

int main(int argc, char* argv[]) {


	int arg1 = 5;
	int arg2 = 10;
	int sum;
	__asm__ (
		"addl %%ebx, %%eax;" // asm source code
		: "=a" (sum) // output
		: "a" (arg1), "b" (arg2) // inputs registers
	);
	printf("Sum is: %d\n", sum); // 15
	
	// OR with asm()
	
	arg1 = 25;
	arg2 = 1000;
	asm(
		"subl %%ebx, %%eax;" // The code itself
		: "=a" (sum) // output
		: "a" (arg1), "b" (arg2) // input registers
	);
	printf("Sum is: %d\n", sum); // -975
}
