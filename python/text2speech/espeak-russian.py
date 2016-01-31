# -*- coding: utf-8 -*-
from espeak import espeak

import codecs
# Install espeak in Ubuntu with
# sudo apt-get instll espeak
# sudo apt-get install python-espeak

# Find the version installed by checking the lib file
# ls /usr/lib/x86_64-linux-gnu/libespeak.so.*
# Or by checking the apt package info
# apt-cache show espeak

# download the full Russian language pack from
# http://espeak.sourceforge.net/data/
# and unzip it and replace the existing russian pack in
# /usr/share/doc/espeak-data

espeak.set_voice("ru")

# Python2 files must be marked # -*- coding: utf-8 -*-
espeak.synth("где папа")

while espeak.is_playing:
	pass
	
