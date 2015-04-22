###############################################################################
#
#  $Id: example2.py 718 2012-04-15 23:59:35Z weegreenblobbie $
#
###############################################################################

# Include the Nsound headers
from Nsound import *

sr = 44100.0

# Create a new instance of the Sine Generator
sine = Sine(sr)

pan = Buffer()

pan << sine.generate(1.0, 3.0)

# Create a stereo AudioStream.
a = AudioStream(sr, 2)

# Fill it with a 220 Hz sine wave.
a << 0.5 * sine.generate(4.9, 220)

# Execute the pan method.
a.pan(pan)

# Write the AudioStream to a wave file
a >> "example2.wav";

pb = AudioPlayback(sr, 2, 16);

a >> pb
