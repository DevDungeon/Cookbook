###############################################################################
#
#  $Id: example3.py 718 2012-04-15 23:59:35Z weegreenblobbie $
#
#  Simulates a drum.  Based on the Csound drum by Hans Mikelson.
#
#  source: http://www.csounds.com/ezine/winter2001/synthesis/
#
###############################################################################

from Nsound import *

sr = 44100.0
BITS_PER_SAMPLE = 16

###############################################################################
def drum(
        duration,
        attack_time,
        high_frequency,
        low_frequency,
        tension,
        resident_frequency):
    "Simple drum"

    sin = Sine(sr)

    frequency_sweep = sin.drawLine(attack_time, high_frequency, low_frequency)

    frequency_sweep << sin.drawLine(
        (duration - attack_time), low_frequency, low_frequency)

    hz_20 = sin.generate(duration, resident_frequency)

    rezzy = hz_20 * frequency_sweep

    parabola = sin.drawParabola(duration, 1.0, duration / 2, 0.25, 0.0)

    rezzy *= parabola

    temp1 = rezzy * tension

    frequency_sweep -= temp1

    audio = sin.generate(duration, frequency_sweep)

    audio *= sin.drawParabola(duration,1.0, 0.5 * duration, 0.3,0.0);

    return audio

###############################################################################

sine = Sine(sr)

bd01 = DrumBD01(sr)
dkb  = DrumKickBass(sr, 266, 0.0)

out = AudioStream(sr, 1);

out << bd01.play() \
    << sine.silence(0.25) \
    << dkb.play() \
    << sine.silence(0.25)

#      duration,  attack, high f, low f, tension, ressonance
out << drum(0.5,   0.012,    160,    51,     0.9,         54) \
    << drum(0.5,   0.012,    160,    51,     0.9,         54) \
    << drum(0.5,   0.012,    160,    51,     0.9,         54) \
    << drum(0.5,   0.012,    160,    51,     0.9,         54) \
    << sine.silence(0.25)

out *= 0.5

hat = Hat(sr)

out << 0.666 * hat.play() << sine.silence(0.25)

out >> "example3.wav"

# ReverberationRoom(sample_rate, room_feedback, wet_percent, dry_percent, low_pass_freq)
room = ReverberationRoom(sr, 0.60, 0.5, 1.0, 100.0)

out2 = 0.5 * room.filter(out)

out2 >> "example3_reverb.wav"

pb = AudioPlayback(sr, 2, 16);

out2 >> pb
