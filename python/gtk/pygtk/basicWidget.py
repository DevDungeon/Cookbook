import pygtk
pygtk.require('2.0')
import gtk

class Base:

    def __init__(self):
        # Init a top level gtkwindow
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.show()

        # Create Button
        self.button = gtk.Button("Hello World")
        
        # Attach callbacks to button, showing multiple
        self.button.connect("clicked", self.hello, None)
        self.button.connect_object("clicked", gtk.Widget.destroy, self.window)

        # Attach generic callbacks
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)

        # This packs the button into the window (a GTK container).
        self.window.add(self.button)
        self.button.show()

    def main(self):
        gtk.main()

    def hello(self, widget, data=None):
        print("Hello world")nn

    # Callback for gtk_destroy_window() (X button)
    def delete_event(self, widget, event, data=None):
        print "Delete event occured."
        # return True if we want to keep window alive
        return False

    # Callback for window destroy cleanup
    def destroy(self, widget, data=None):
        gtk.main_quit()
        
if __name__ == "__main__":
    base = Base()
    base.main()
