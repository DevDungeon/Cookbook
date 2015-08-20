# sudo apt-get install libnotify-bin python-gobject
from gi.repository import Notify

Notify.init ("App name")
Hello = Notify.Notification.new (
    "Hello world","This is an example notification.","dialog-information")
Hello.show ()
