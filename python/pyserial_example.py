# pip install pyserial
import serial

dev = serial.Serial('COM7')

while True:
    print(dev.readline())