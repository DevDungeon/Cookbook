#!/usr/bin/python2

from gi.repository import Gtk
import os

# Settings
glade_file = os.path.dirname(os.path.realpath(__file__)) + "/dash.glade"
vhosts_file = '/etc/httpd/conf/extra/httpd-vhosts.conf'
ehosts_file = '/etc/hosts'
apache_restart_command = 'systemctl restart httpd'


class NanoDash:
    """
    Gtk Builder and main top level window
    Sets up event handling and shows windows
    """
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(glade_file)

        handlers = {
            "deleteMainWindow": self.deleteMainWindow,
            "openAboutWin": self.openAboutWin,
            "ehostsSave": self.ehostsSave,
            "vhostsSave": self.vhostsSave,
            "restartHttpd": self.restartHttpd,
        }
        self.builder.connect_signals(handlers)

        self.mainWin = self.builder.get_object("MainWindow")
        self.mainWin.show_all()

        # Fill the hosts TextView with /etc/hosts file
        self.ehostsTextView = self.builder.get_object("ehostsText")
        self.ehostsBuff = self.ehostsTextView.get_buffer()
        with open(ehosts_file, "r") as hostsFile:
            self.ehostsBuff.set_text(hostsFile.read())
        # Set ehost scrolled window to expand on resize
        self.ehostsScrollWin = self.builder.get_object("ehostsScrollWin")
        self.ehostsScrollWin.set_hexpand(True)
        self.ehostsScrollWin.set_vexpand(True)

        # Fill the vhosts
        self.vhostsTextView = self.builder.get_object("vhostsText")
        self.vhostsBuff = self.vhostsTextView.get_buffer()
        with open(vhosts_file, "r") as hostsFile:
            self.vhostsBuff.set_text(hostsFile.read())
        # Set vhost scrolled window to expand on resize
        self.vhostsScrollWin = self.builder.get_object("vhostsScrollWin")
        self.vhostsScrollWin.set_hexpand(True)
        self.vhostsScrollWin.set_vexpand(True)

    def restartHttpd(self, *args):
        print("restarting apache")
        print(os.system(apache_restart_command))

    def run(self):
        Gtk.main()

    def openAboutWin(self, *args):
        self.aboutWin = self.builder.get_object("aboutdialog1")
        self.aboutWin.show_all()

    def deleteMainWindow(self, *args):
        Gtk.main_quit(*args)

    def ehostsSave(self, *args):
        ehostsText = self.ehostsBuff.get_text(self.ehostsBuff.get_start_iter(),
                                       self.ehostsBuff.get_end_iter(),
                                       False)
        f = open(ehosts_file, 'w+')
        f.write(ehostsText)
        f.close()

    def vhostsSave(self, *args):
        vhostsText = self.vhostsBuff.get_text(self.vhostsBuff.get_start_iter(),
                                       self.vhostsBuff.get_end_iter(),
                                       False)
        f = open(vhosts_file, 'w+')
        f.write(vhostsText)
        f.close()

if __name__ == "__main__":
    dash = NanoDash()
    dash.run()
