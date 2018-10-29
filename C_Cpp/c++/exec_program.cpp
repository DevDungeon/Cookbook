/**
 * exec_program.cpp
 * 
 * gcc exec_program.cpp
 * 
 * Demonstrates how to execute a program using the system.
 * 
 */

// popen
// system/exec
// create process?
// win vs linux?
    // Windows API: ShellExecute

// get self pid
// get forked pid
// get output
// pause it
// dump memory of process?
// send input
// get return value

// Replace current process with another
// execl("/bin/ls", "ls", "-r", "-t", "-l", (char *) 0);

// Option B) Fork and then exec manually
// Fork to create a copy of the current process
// then check pid to see if its parent or child process
// if child process, exec process, which REPLACES the process
 // int pid = fork();
// cout << pid << endl;
//fork() returns the process identifier (pid) of the child process in the parent, and
//fork() returns 0 in the child.
// if (pid==0) {
//     execl("/bin/ls", "ls", "-r", "-t", "-l", (char *) 0);
http://man7.org/linux/man-pages/man3/exec.3.html
// this is how you create a runner/wrapper for an exe file
// but how to EMBED the binary file inside and jump directly to it? - put it in memory and point to it literally? can I point to spot on disk? nope.
execl, execlp, execle, execv, execvp, execvpe - execute a file
//execvp?
// }
// cout << "done" << endl;

// fork and exec a new process
// popen()


