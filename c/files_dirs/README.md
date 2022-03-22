#include <unistd.h>

char *getcwd(char *buf, size_t size);

char cwd[PATH_MAX]
if (getcwd(cwd, sizeof(cwd)) != NULL) { /*success*/ }
