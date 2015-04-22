#!/usr/bin/python2
"""
PyAudio Example: Make a wire between input and output (i.e., record a
few samples and play them back immediately).
"""

# Stream audio from one source to another
# In this case takes default in and also writes
# that stream to default out -  With a default
# mic/speaker setup this echos mic to speakers

import pyaudio

CHUNK = 1024
WIDTH = 2
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

print("* recording")

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    stream.write(data, CHUNK)

print("* done")

stream.stop_stream()
stream.close()

p.terminate()
