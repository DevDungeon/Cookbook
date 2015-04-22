#!/usr/bin/python

#// dependency libnotify, python-gobject
from gi.repository import Notify

Notify.init ("Hello world")
Hello = Notify.Notification.new (
    "Hello world","This is an example notification.","dialog-information")
Hello.show ()
