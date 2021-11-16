import serial
import time
import study_load
import study_shuffle

arduino = serial.Serial(port='/dev/cu.usbmodem101', baudrate=9600, timeout=1)

def write_data(x):
    try:
        arduino.write(bytes(x, 'utf-8'))
    except serial.SerialException:
        time.sleep(0.1)
    
    time.sleep(0.5)

def read_data():
    try:
        arduino.flushInput()
    except Exception as e:
        time.sleep(0.1)
    data = arduino.readline().decode("utf-8")
    return data

# Load all YouTube Urls
browser = study_load.driverSetup()
categories = study_load.loadUrls(browser)
queries = ['anime', 'beach', 'window', 'r&b', 'white noise']

buttonTrigger = '1'
left = set("2".split())
up = set("3".split())
right = set("4".split())
down = set("5".split())
six = set("6".split())

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
        
        if set1 == left:
            choice = 1
        elif set1 == up:
            choice = 2
        elif set1 == right:
            choice = 3
        elif set1 == down:
            choice = 4
        elif set1 == six:
            choice = 5
        if choice != 0:
            # Enable button
            write_data("b")
            print(queries[choice-1] + " chosen")
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
    write_data("g")
    study_shuffle.shuffle(categories, choice)