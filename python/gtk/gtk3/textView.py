from gi.repository import Gtk

glade_file = "textView.glade"

class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

class MainWindow:

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(glade_file)
        self.builder.connect_signals(Handler())
        self.win = self.builder.get_object("window1")
        self.win.show_all()

        # Fill the hosts TextView with /etc/hosts file
        self.hostsTextView = self.builder.get_object("textview1")
        self.hostsBuff = self.hostsTextView.get_buffer()
        with open("/etc/hosts", "r") as hostsFile:
            self.hostsBuff.set_text(hostsFile.read())

if __name__ == "__main__":
    mainWin = MainWindow()
    Gtk.main()
