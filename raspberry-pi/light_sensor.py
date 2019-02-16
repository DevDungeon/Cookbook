"""
Light sensor example

Pin number is the physical pin number
Connect one end of light sensor to power/3.3v
Connect other end of light sensor to GPIO input,
  but also with a 1uF capacitor in line to the ground
  (negative end in ground if polarized capacitor)

Print out the time between capacitor charges. Quick time
means lots of lights, long time means low light.

######
This basically discharges the capacitor and then recharges it, measuring
the delay (in non-real Python time) before the capacitor reaches enough
voltage to register as a digital HIGH. Inaccurate, but good enough for
some relative values.
"""
import RPi.GPIO as GPIO
import time

__author__ = 'Gus (Adapted from Adafruit)'
__license__ = "GPL"
__maintainer__ = "pimylifeup.com"

GPIO.setmode(GPIO.BOARD)

#define the pin that goes to the circuit
pin_to_circuit = 24

def rc_time (pin_to_circuit):
    count = 0

    #Output on the pin for
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)

    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

#Catch when script is interupted, cleanup correctly
try:
    # Main loop
    while True:
        print rc_time(pin_to_circuit)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
