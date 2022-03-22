#include <libnotify/notify.h>
// sudo apt install libnotify-dev

// Compile with
// gcc -o notify  `pkg-config --cflags --libs libnotify` libnotify.c

void main () {
	notify_init ("Hello world!");
	NotifyNotification * Hello = notify_notification_new ("Hello world", "This is an example notification.", "dialog-information");
	notify_notification_show (Hello, NULL);
//	g_object_unref(G_OBJECT(Hello));
//	notify_uninit();
}
