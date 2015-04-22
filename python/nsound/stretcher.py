###############################################################################
#
#  $Id: stretcher.py 585 2010-12-15 05:21:28Z weegreenblobbie $
#
###############################################################################

from Nsound import *

# Read in the wavefile.
a1 = AudioStream("Temperature_in.wav")

# Grab sample rate.
sr = a1.getSampleRate()

# Grab the duration in seconds.
duration = a1.getDuration()

# Create a Gaussian curve for pitch/time shifting.
sin = Sine(sr)

bend = Buffer()
bend << sin.drawFatGaussian(duration, 0.15) + 1.0

# Create a Stretcher instance
stretch = Stretcher(sr, 0.08, 0.25)

# Print progress to command line.
stretch.showProgress(True)

print "Pitch Shifting Up"

# Create new output AudioStream.
out = AudioStream(sr, 2)

# Pitch shift the input AudioStream.
out << stretch.pitchShift(a1, bend)
out >> "Temperature_Pitch_Shifted_Up.wav"

print "Time Shifting Faster"

# Time shift input AudioStream
out = AudioStream(sr,2)
out << stretch.timeShift(a1, 1.0 / bend)
out >> "Temperature_Time_Shifted_Faster.wav"

bend = Buffer()
bend << 1.0 - 0.25 * sin.drawFatGaussian(duration, 0.15)

print "Pitch Shifting Down"

out = AudioStream(sr, 2)
out << stretch.pitchShift(a1, bend)
out >> "Temperature_Pitch_Shifted_Down.wav"

print "Time Shifting Slower"

bend = Buffer()
bend << 1.0 + 0.75 * sin.drawFatGaussian(duration, 0.15)

out = AudioStream(sr, 2)
out << stretch.timeShift(a1, bend)
out >> "Temperature_Time_Shifted_Slower.wav"
