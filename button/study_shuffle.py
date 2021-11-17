from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
import random
import time
from threading import Timer
import notification
import serial

arduino = serial.Serial(port='/dev/cu.usbmodem101', baudrate=9600, timeout=1)

def write_data(x):
    try:
        arduino.write(bytes(x, 'utf-8'))
    except serial.SerialException:
        time.sleep(0.1)
    time.sleep(0.5)

def breaktime():
    # Flash light to signal last 5 seconds
    write_data("f")
    write_data("r")
    message = "Time for a 5 minute break!"
    print(message)
    notification.alert(message, True)


def studytime():
    # Flash light to signal last 5 seconds
    write_data("f")
    write_data("g")
    message = "Back to studying!"
    print(message)
    notification.alert(message, False)



def shuffle(categories, choice):

    queries = ['anime', 'beach', 'window', 'r&b', 'white noise']

    # Pick a category
    num = choice
    if num == 1:    # Anime
        query = queries[0]
    elif num == 2:  # Beach
        query = queries[1]
    elif num == 3:  # Window
        query = queries[2]
    elif num == 4:           # R&B
        query = queries[3]
    else: query = queries[4]

    categoryNum = num -1
    # Select a random video
    rand = random.randint(0,len(categories[categoryNum].urls)-1)
    # Parse for YouTube video ID
    videoID = categories[categoryNum].urls[rand].split('=')
    # Open video in browser and play it
    print("๑ ⋆˚₊⋆────ʚ "+"Playing " + query + " video #" + str(rand+1)+" ɞ────⋆˚₊⋆ ๑")
    serv = Service('./chromedriver')
    browser = webdriver.Chrome(service=serv)
    browser.get('https://www.youtube.com/embed/' + videoID[1] + '?autoplay=1&cc_load_policy=1')
    try:
        # While browser is running and not quit
        while(browser.title):
            # duration is in seconds
            studying = Timer(20, breaktime)
            studying.start()

            # wait for time completion
            studying.join()
            # check if browser is still open
            browser.title
            # duration is in seconds
            breaking = Timer(5, studytime)
            breaking.start()

            # wait for time completion
            breaking.join()
    except Exception as e:
        breaking.cancel()
        studying.cancel()
        #print("Exception:")
