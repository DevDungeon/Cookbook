// The functions contained in this file are pretty dummy
// and are included only as a placeholder. Nevertheless,
// they *will* get included in the static library if you
// don't remove them :)
// 
// Obviously, you 'll have to write yourself the super-duper
// functions to include in the resulting library...
// Also, it's not necessary to write every function in this file.
// Feel free to add more files in this project. They will be
// included in the resulting library.

// gcc -c -o out.o out.c
//  -c means to create an intermediary object file, rather than an executable.
// ar rcs libout.a out.o
// This creates the static library.  r means to insert with replacement,
//   c means to create a new archive, and s means to write an index.

// A function adding two integers and returning the result
int SampleAddInt(int i1, int i2)
{
    return i1 + i2;
}

// A function doing nothing ;)
void SampleFunction1()
{
    // insert code here
}

// A function always returning zero
int SampleFunction2()
{
    // insert code here
    
    return 0;
}
