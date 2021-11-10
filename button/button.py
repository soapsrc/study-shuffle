## Code obtained from https://create.arduino.cc/projecthub/ansh2919/serial-communication-between-python-and-arduino-e7cce0

import serial
import time
import re

trigger = '1'

arduino = serial.Serial(port='/dev/cu.usbmodem1101', baudrate=9600, timeout=.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

def read_data():
    data = arduino.readline().decode("utf-8")
    #print(data)
    return data

while True:
    time.sleep(1)
    value = read_data()
    set1 = set(value.split())
    set2 = set(trigger.split())
    if(set1 == set2):
        print("Button pressed")
