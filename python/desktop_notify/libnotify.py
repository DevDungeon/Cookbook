# 03 Combined
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify, GdkPixbuf
Notify.init("My App")


notification = Notify.Notification.new("summary", "body\nbody<strong>t</strong>\n<a href=\"\">test</a><em>test</em><u>asdf</u><img src="">", "/home/nanodano/logo.png")
notification.set_urgency(1)
notification.show()

import os
os.system("notify-send test test")

import subprocess
subprocess.call(['notify-send', 'summary', 'body'])


Notify.uninit()