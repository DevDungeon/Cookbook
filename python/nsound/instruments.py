###############################################################################
#
#  $Id: example4.py 718 2012-04-15 23:59:35Z weegreenblobbie $
#
###############################################################################

from Nsound import *

sr = 44100.0

sine = Sine(sr)

bass = GuitarBass(sr)
slide = FluteSlide(sr)
clarinet = Clarinet(sr)

out = AudioStream(sr, 1)

out << bass.play()      << sine.silence(1.0) \
    << slide.play()     << sine.silence(1.0) \
    << clarinet.play()  << sine.silence(1.0)

out *= 0.5

# Set the default Wavefile sample size and rate.
Wavefile.setDefaults(sr, 16)

out >> "example4.wav"

room = ReverberationRoom(sr, 0.9); # 0.9 = room feed back (0.0 to 1.0)

out2 = room.filter(0.5 * (bass.play() << sine.silence(1.5)))

out2 >> "example4_reverb.wav"

# Play to audio device.

pb = AudioPlayback(sr, 2, 16)

out >> pb
out2 >> pb
