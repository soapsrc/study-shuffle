from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
import random
import time
from threading import Timer
import pygame

def breaktime():
    print("Time for a 5 minute break!")
    pygame.mixer.init()
    pygame.mixer.music.load("break.mp3")
    pygame.mixer.music.play()

def studytime():
    print("Time for a 5 minute break!")
    pygame.mixer.init()
    pygame.mixer.music.load("study.mp3")
    pygame.mixer.music.play()


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
            t = Timer(20, breaktime)
            t.start()

            # wait for time completion
            t.join()
    except Exception as e:
        time.sleep(0.1)
        #print("Exception:")
