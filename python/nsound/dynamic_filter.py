###############################################################################
#
#  $Id: dynamic_filter.py 361 2009-09-10 00:37:56Z weegreenblobbie $
#
###############################################################################

from Nsound import *

# Read in the wavefile.
input = AudioStream("Temperature_in.wav")

# Grab the duration in seconds.
duration = input.getDuration()

# Create a low pass filter with a kernel of 256 terms.
lpf = FilterLowPassFIR(input.getSampleRate(), 256, 100)

# Create a buffer that will hold cut off frequencies.
frequencies = Buffer()

# Fill it with two lines
sin = Sine(input.getSampleRate())

frequencies << sin.drawLine(0.5 * duration, 8000, 50) \
            << sin.drawLine(0.5 * duration, 50, 8000)

# Filter it.
output = lpf.filter(input, frequencies)

# Write to disk.
output >> "Temperature_out.wav"

