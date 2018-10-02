# pip install pyttsx3
# pip install pypiwin32
import pyttsx3

engine = pyttsx3.init()

engine.say("Hello, world!")

engine.setProperty('rate', 100)  # Speed percent (can go over 100)
engine.setProperty('volume', 0.8)  # Volume 0-1

engine.runAndWait()