#include <syslog.h>

// view with:
// journalctl
// of
// journalctl -f

// for more help see: man syslog
void main() {
    //void syslog(int priority, const char *message, arguments...);
    // %m will be error message or "Success"
    syslog(LOG_INFO, "My test log entry!! %m\n");
}
