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

# Button will ouput '1' if pressed
trigger = '1'

while True:
    buttonPressed = False
    #Enable button
    write_data("Button enabled")
    print("๑ ⋆˚₊⋆────ʚ Enter 1 to press the button and continue ɞ────⋆˚₊⋆ ๑")
    # Wait until the button is pressed
    while not buttonPressed:
        value = read_data()
        # Check if the button has been pressed
        set1 = set(value.split())
        set2 = set(trigger.split())
        if(set1 == set2):
            # Disable button while video is playing
            write_data("Button disabled")
            buttonPressed = True
    # Play random ambience video from YouTube
    study_shuffle.shuffle(categories)