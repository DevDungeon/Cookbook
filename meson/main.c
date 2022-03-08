// https://mesonbuild.com/Tutorial.html
#include <gtk/gtk.h> // `pkgconfig --cflags --libs gtk+-3.0`

//
// Should provided the active view for a GTK application
//
static void activate(GtkApplication* app, gpointer user_data)
{
  GtkWidget *window;
  GtkWidget *label;

  window = gtk_application_window_new (app);
  label = gtk_label_new("Hello GNOME!");
  gtk_container_add (GTK_CONTAINER (window), label);
  gtk_window_set_title(GTK_WINDOW (window), "Welcome to GNOME");
  gtk_window_set_default_size(GTK_WINDOW (window), 200, 100);
  gtk_widget_show_all(window);
} // end of function activate

//
// main is where all program execution starts
//
int main(int argc, char **argv)
{
  GtkApplication *app;
  int status;

  app = gtk_application_new(NULL, G_APPLICATION_FLAGS_NONE);
  g_signal_connect(app, "activate", G_CALLBACK(activate), NULL);
  status = g_application_run(G_APPLICATION(app), argc, argv);
  g_object_unref(app);

  return status;
} // end of function main

