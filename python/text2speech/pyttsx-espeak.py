#!/usr/bin/python2
import pyttsx

engine = pyttsx.init("espeak")
engine.setProperty('rate', 150)
engine.setProperty('voice', 'en-us')

engine.say('Howdy yall, whats happening!')
engine.say('Howdy again!')

engine.runAndWait()
