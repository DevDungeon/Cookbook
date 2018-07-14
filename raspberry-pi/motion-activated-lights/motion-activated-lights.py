"""
Wiring setup:
- PIR sensor - GPIO 1
- Power relay output - GPIO 2
"""


# If PIR_GPIO_PIN is on
    # Turn on GPIO 2


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)


PIR_INPUT_PIN = 18
POWER_RELAY_PIN = 12





if __name__ == '__main__':
    GPIO.setup(PIR_INPUT_PIN, GPIO.IN)
    GPIO.setup(POWER_RELAY_PIN, GPIO.OUT)

    try:
        while True:
        GPIO.output(port_or_pin, 1)
            if GPIO.input(PIR_INPUT_PIN) == 1:
                print("Motion detected.")
                GPIO.output(POWER_RELAY_PIN, 1)
    except KeyboardInterrupt:
        print("[*] Keyboard interrupt received. Exiting.")
    except Exception as e:
        print("[-] Unexpected error.")
        print(e)
    finally:
        GPIO.cleanup()

