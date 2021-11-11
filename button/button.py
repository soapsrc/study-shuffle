import serial
import time
import study_load
import study_shuffle

arduino = serial.Serial(port='/dev/cu.usbmodem101', baudrate=9600, timeout=1)

def write_data(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.5)

def read_data():
    arduino.flushInput()
    data = arduino.readline().decode("utf-8")
    return data

# Load all YouTube Urls
browser = study_load.driverSetup()
categories = study_load.loadUrls(browser)

buttonTrigger = '1'

while True:
    joyMoved = False
    buttonPressed = False
    choice = 0
    #Enable joystick
    write_data("j")
    print("๑ ⋆˚₊⋆────ʚ Pick a category to continue ɞ────⋆˚₊⋆ ๑")
    while not buttonPressed:
        try:
            value = read_data()
        except serial.SerialException:
            time.sleep(0.1)
        set1 = set(value.split())
        left = set("2".split())
        up = set("3".split())
        right = set("4".split())
        down = set("5".split())
        if set1 == left:
            choice = 1
        elif set1 == up:
            choice = 2
        elif set1 == right:
            choice = 3
        elif set1 == down:
            choice = 4
        if choice != 0:
            # Enable button
            write_data("b")
        try:
            value = read_data()
        except serial.SerialException:
            time.sleep(0.1)
        set1 = set(value.split())
        set2 = set(buttonTrigger.split())
        if set1 == set2 and choice != 0:
            # Disable button and joystick
            write_data("d")
            buttonPressed = True
    study_shuffle.shuffle(categories, choice)