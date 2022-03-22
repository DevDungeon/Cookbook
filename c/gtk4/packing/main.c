/**
Reference:
https://docs.gtk.org/gtk4/

Compile with:
gcc $( pkg-config --cflags gtk4 ) main.c $( pkg-config --libs gtk4 )
*/ 
#include <gtk/gtk.h>
#include <string.h>
#include <stdio.h>

typedef struct {
	GtkTextBuffer* textbuffer;
	GtkTextView* textview;
} BtnCallbackData;

static void
print_hello (GtkWidget *widget,
             gpointer   data)
{

	BtnCallbackData* callback_data = (BtnCallbackData*)data;
	
  //printf("Cast data to whatever? %p\n", GTK_TEXT_BUFFER(temp_data.textbuffer);
  g_print ("Hello World\n"); // debug print
  g_print("%p address of textview inside", callback_data->textview);
  	const char text[16] = "Button clicked!";
	//GtkTextBuffer* textbuffer = gtk_text_view_get_buffer(GTK_TEXT_VIEW(callback_data->textview)); // https://docs.gtk.org/gtk4/property.TextView.buffer.html
	gtk_text_buffer_set_text(callback_data->textbuffer, text, strlen(text));
	
	//GtkTextIter* buff_iter;
	//gtk_text_buffer_get_end_iter(GTK_TEXT_BUFFER(data), buff_iter);
	//gtk_text_buffer_insert(GTK_TEXT_BUFFER(data), buff_iter, "CLICKED! ", 9);

}

static void
activate (GtkApplication *app,
          gpointer        user_data)
{
	// Get main window
	GtkWidget* window = gtk_application_window_new(app);
	gtk_window_set_title (GTK_WINDOW(window), "Window");
	gtk_window_set_default_size (GTK_WINDOW(window), 200, 200);

	// Create a simple box container and attach to window
	GtkWidget* box = gtk_box_new (GTK_ORIENTATION_VERTICAL, 0);
	gtk_window_set_child (GTK_WINDOW(window), box);

    
	

	// Create text editor and pack into box
	GtkWidget* textview = gtk_text_view_new(); // https://docs.gtk.org/gtk4/method.TextView.get_buffer.html
	gtk_box_append(GTK_BOX(box), textview);
	// Set the text of the editor's buffer
	const char text[16] = "Hello, world!";
	GtkTextBuffer* textbuffer = gtk_text_view_get_buffer(GTK_TEXT_VIEW(textview)); // https://docs.gtk.org/gtk4/property.TextView.buffer.html
	gtk_text_buffer_set_text(textbuffer, text, strlen(text));
	
	// Create a button, connect a callback, and pack in container
	// Passing the textbuffer as an argument to the function
	GtkWidget* button = gtk_button_new_with_label ("Hello World");
	BtnCallbackData callback_data;
	callback_data.textview = GTK_TEXT_VIEW(textview);
	callback_data.textbuffer = textbuffer;
	g_signal_connect (button, "clicked", G_CALLBACK(print_hello), &callback_data);
	
	g_print("%p address of textview outside", callback_data.textview);
	
// https://docs.gtk.org/gtk4/method.TextBuffer.set_text.html

/*
 * void
gtk_text_buffer_set_text (
  GtkTextBuffer* buffer,
  const char* text,
  int len
)
* */
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  



	gtk_box_append (GTK_BOX (box), button);

	gtk_widget_show (window);
}

int
main (int    argc,
      char **argv)
{
  GtkApplication *app;
  int status;

  app = gtk_application_new ("org.gtk.example", G_APPLICATION_FLAGS_NONE);
  g_signal_connect (app, "activate", G_CALLBACK (activate), NULL);
  status = g_application_run (G_APPLICATION (app), argc, argv);
  g_object_unref (app);

  return status;
}

