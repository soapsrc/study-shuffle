### Arduino simiulator that runs the study-shuffle program
### The same logic as button.py except that it takes user input from the command line instead of the Arduino interface

import time
import study_load
import study_shuffle

def write_data(x):
    print(x)
    time.sleep(0.05)

def read_data():
    data = input("")
    #if(len(data) > 0):
        #print(data)
    return data

# Disable button while loading data
write_data("Button disabled")

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
    study_shuffle.shuffle(categories, choice)