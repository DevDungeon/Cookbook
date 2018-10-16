"""
Soil moisture sensor example

Plug two wires on to the end of the soil moisture sensor. Polarity does not matter.
Connect the other end of the wires to the 2 prong adapter on the chip board
that came with the moisture sensor.


"""
import RPi.GPIO as GPIO
import time

__author__ = 'Gus (Adapted from Adafruit)'
__license__ = "GPL"
__maintainer__ = "pimylifeup.com"

GPIO.setmode(GPIO.BOARD)


digital_out_pin = 18  # DO pin from soil moisture board
analog_out_pin = 12  # AO pin from soil moisture board


def print_status_of_soil_sensor():
    print("Digital pin: %d" % GPIO.input(digital_out_pin))
    print("Analog pin: %d" % GPIO.input(analog_out_pin))


if __name__ == '__main__':
    GPIO.setup(digital_out_pin, GPIO.IN)
    GPIO.setup(analog_out_pin, GPIO.IN)

    try:
        while True:
            print_status_of_soil_sensor()
            time.sleep(1)

    except KeyboardInterrupt:
        print("[*] Keyboard interrupt received. Exiting.")
    finally:
        GPIO.cleanup()
