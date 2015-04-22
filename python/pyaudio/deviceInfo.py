#!/usr/bin/python2
import pyaudio
""" Get info about devices """

p = pyaudio.PyAudio()

inDev = p.get_default_input_device_info()
print(inDev)

outDev = p.get_default_input_device_info()
print(outDev)

devCount = p.get_device_count()
print("Number of devices: " + repr(devCount))

p.terminate()
