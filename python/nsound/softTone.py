###############################################################################
#
#  $Id: example6.py 718 2012-04-15 23:59:35Z weegreenblobbie $
#
###############################################################################

from Nsound import *

sr = 44100.0;
BITS_PER_SAMPLE = 16;

###############################################################################
def softTones(sr, duration, f1, f2, gaussian_width):

    sin = Sine(sr)

    audio = AudioStream(sr, 2)

    envelope = sin.drawFatGaussian(duration, gaussian_width)

    audio[0] = sin.generate(duration, f1)
    audio[1] = sin.generate(duration, f2)

    return audio * envelope

###############################################################################
# Main
sine = Sine(sr)

out = AudioStream(sr, 2)

out << softTones(sr, 0.25, 261.63, 523.25, 0.90) \
    << softTones(sr, 0.25, 493.87, 293.66, 0.90) \
    << softTones(sr, 0.25, 329.61, 439.96, 0.90) \
    << softTones(sr, 0.25, 391.97, 349.22, 0.90) \
    << softTones(sr, 0.25, 349.22, 391.97, 0.90) \
    << softTones(sr, 0.25, 439.96, 329.61, 0.90) \
    << softTones(sr, 0.25, 293.66, 493.87, 0.90) \
    << softTones(sr, 0.25, 523.25, 261.63, 0.90) \
    << softTones(sr, 0.25, 261.63, 523.25, 0.90) \
    << softTones(sr, 0.25, 493.87, 293.66, 0.90) \
    << softTones(sr, 0.25, 329.61, 439.96, 0.90) \
    << softTones(sr, 0.25, 391.97, 349.22, 0.90) \
    << softTones(sr, 0.25, 349.22, 391.97, 0.90) \
    << softTones(sr, 0.25, 439.96, 329.61, 0.90) \
    << softTones(sr, 0.25, 293.66, 493.87, 0.90) \
    << softTones(sr, 0.25, 523.25, 261.63, 0.90) \
    << sine.silence(0.25)

out << softTones(sr, 0.25, 261.63, 523.25, 0.30) \
    << softTones(sr, 0.25, 493.87, 293.66, 0.30) \
    << softTones(sr, 0.25, 329.61, 439.96, 0.30) \
    << softTones(sr, 0.25, 391.97, 349.22, 0.30) \
    << softTones(sr, 0.25, 349.22, 391.97, 0.30) \
    << softTones(sr, 0.25, 439.96, 329.61, 0.30) \
    << softTones(sr, 0.25, 293.66, 493.87, 0.30) \
    << softTones(sr, 0.25, 523.25, 261.63, 0.30) \
    << softTones(sr, 0.25, 261.63, 523.25, 0.30) \
    << softTones(sr, 0.25, 493.87, 293.66, 0.30) \
    << softTones(sr, 0.25, 329.61, 439.96, 0.30) \
    << softTones(sr, 0.25, 391.97, 349.22, 0.30) \
    << softTones(sr, 0.25, 349.22, 391.97, 0.30) \
    << softTones(sr, 0.25, 439.96, 329.61, 0.30) \
    << softTones(sr, 0.25, 293.66, 493.87, 0.30) \
    << softTones(sr, 0.25, 523.25, 261.63, 0.30) \
    << sine.silence(0.25)

out *= 0.5

out >> "example6.wav"

# ReverberationRoom(sample_rate, room_feedback, wet_percent, dry_percent, low_pass_freq)
room = ReverberationRoom(sr, 0.50, 1.0, 1.0, 100.0)

out2 = 0.5 * room.filter(out)

out2 >> "example6_reverb.wav"

pb = AudioPlayback(sr, 2, 16)

out2 >> pb
