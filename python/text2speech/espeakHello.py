#!/usr/bin/python2
"""
espeak bindings for python2 
https://launchpad.net/python-espeak
Arch Linux - AUR: python2-espeak
"""

from espeak import espeak

espeak.set_voice("en-us")
espeak.synth("Hello, world!")

# Prevents sound from cutting off since program ends
while (espeak.is_playing()):
	continue

#espeak.cancel() # Stop speaking
#espeak.set_voice("en-us")
#print(espeak.list_voices())
