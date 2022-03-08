/**
Reference:
https://riptutorial.com/gtk3/example/18820/-c---hello-world--in-gtkplus
https://docs.gtk.org/gtk3/

Compile with:
gcc main.c `pkg-config --cflags --libs gtk+-3.0`
*/ 
#include <gtk/gtk.h>
// https://gitlab.gnome.org/GNOME/gtk/-/blob/gtk-3-24/gtk/gtk.h


// callback function which is called when application is first started
static void on_app_activate(GApplication* app, gpointer data) {
    // create a new application window for the application
    // GtkApplication is sub-class of GApplication
    // downcast GApplication* to GtkApplication* with GTK_APPLICATION() macro
    GtkWidget* window = gtk_application_window_new(GTK_APPLICATION(app));
    // display the window
    gtk_widget_show_all(GTK_WIDGET(window));
}

int main(int argc, char *argv[]) {
    // https://docs.gtk.org/gtk3/ctor.Application.new.html
    GtkApplication* app = gtk_application_new(
        "com.example.MyApp", 
        G_APPLICATION_FLAGS_NONE
    );

    // connect the event-handler for "activate" signal of GApplication
    // G_CALLBACK() macro is used to cast the callback function pointer
    // to generic void pointer
    g_signal_connect(app, "activate", G_CALLBACK(on_app_activate), NULL);
    
    // start the application, terminate by closing the window
    // GtkApplication* is upcast to GApplication* with G_APPLICATION() macro
    int status = g_application_run(G_APPLICATION(app), argc, argv);
    
    // Cleanup
    g_object_unref(app);
    return status;
}
