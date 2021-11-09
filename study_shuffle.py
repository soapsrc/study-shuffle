from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
import random
import study_load

browser = study_load.driverSetup()
categories = study_load.loadUrls(browser)

# Pick a category
num = int(input("1 - Anime\n2 - Beach\n3 - Window\n4 - R&B\nEnter the number associated to the video category you want to study to\n"))
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
rand = random.randint(0,len(categories[categoryNum].urls))
# Parse for YouTube video ID
videoID = categories[categoryNum].urls[rand].split('=')
# Open video in browser and play it
print("Playing " + query + " video #" + str(rand))
browser = webdriver.Chrome(service=serv)
browser.get('https://www.youtube.com/embed/' + videoID[1] + '?autoplay=1')
