## Code obtained from https://create.arduino.cc/projecthub/ansh2919/serial-communication-between-python-and-arduino-e7cce0

import serial
import time
import study_load
import study_shuffle

arduino = serial.Serial(port='/dev/cu.usbmodem101', baudrate=9600, timeout=5)

def write_data(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)

def read_data():
    arduino.flushInput()
    data = arduino.readline().decode("utf-8")
    #if(len(data) > 0):
        #print(data)
    return data

# Load all YouTube Urls
browser = study_load.driverSetup()
categories = study_load.loadUrls(browser)

trigger = '1'

while True:
    buttonPressed = False
    print("๑ ⋆˚₊⋆────ʚ Press the button to continue ɞ────⋆˚₊⋆ ๑")
    #Enable button
    write_data("e")
    while not buttonPressed:
        value = read_data()
        set1 = set(value.split())
        set2 = set(trigger.split())
        if(set1 == set2):
            # Disable button
            write_data("d")
            buttonPressed = True
    study_shuffle.shuffle(categories)