from gi.repository import Gtk

class HelloWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        self.button = Gtk.Button(label="Hello!")
        self.button.connect("clicked", self.sayHello)
        self.add(self.button)

    def sayHello(self, widget):
        print("Hello World")

win = HelloWindow()
# Attach Gtk quit to exit of this window, what an important window!
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
