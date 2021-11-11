from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
import random
import time


def shuffle(categories, choice):

    # Pick a category
    num = choice
    if num == 1:    # Anime
        query = "anime"
    elif num == 2:  # Beach
        query = "beach"
    elif num == 3:  # Window
        query = "window"
    else:           # R&B
        query = "rnb"

    categoryNum = num -1
    # Select a random video
    rand = random.randint(0,len(categories[categoryNum].urls)-1)
    # Parse for YouTube video ID
    videoID = categories[categoryNum].urls[rand].split('=')
    # Open video in browser and play it
    print("๑ ⋆˚₊⋆────ʚ "+"Playing " + query + " video #" + str(rand+1)+" ɞ────⋆˚₊⋆ ๑")
    serv = Service('./chromedriver')
    browser = webdriver.Chrome(service=serv)
    browser.get('https://www.youtube.com/embed/' + videoID[1] + '?autoplay=1')
    try:
        # While browser is running and not quit
        while(browser.title):
            time.sleep(1)
    except Exception as e:
        time.sleep(0.1)
        #print("Browser closed")
