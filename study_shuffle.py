from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import random
import time

# Hides the browser window containing the search results
co = webdriver.ChromeOptions()
co.add_argument('headless')
co.add_argument('window-size=1920x1080')
co.add_argument("disable-gpu")
# Path to webdriver
serv = Service('./chromedriver')
browser = webdriver.Chrome(service=serv, options=co)

queries = ['anime', 'beach', 'window', 'r&b']
hrefs = []
category1 = []
category2 = []
category3 = []
category4 = []
allUrls = [category1, category2, category3, category4]

# For each category, save the the relevant YouTube video urls to the appropriate array
for i in range(0, len(queries)):
    print("Storing all " + queries[i] + " urls")
    url = 'https://www.youtube.com/results?search_query=' + queries[i] + '+study+ambience'
    browser.get(url)
    # Parse html of webpage
    source = browser.page_source
    soup = BeautifulSoup(source,'html.parser')
    browser.get(url)
    # Find the YouTube urls of all the videos that resulted from each query
    hrefs = soup.find_all("a", class_="yt-simple-endpoint style-scope ytd-video-renderer")
    for a in hrefs:
        allUrls[i].append(a['href'])
    print(allUrls[i])
    # Sleep for 2 seconds to make sure webpage has been thoroughly parsed
    time.sleep(2)

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
rand = random.randint(0,len(allUrls[categoryNum]))
# Parse for YouTube video ID
videoID = allUrls[categoryNum][rand].split('=')
# Open video in browser and play it
print("Playing " + query + " video #" + str(rand))
browser = webdriver.Chrome(service=serv)
browser.get('https://www.youtube.com/embed/' + videoID[1] + '?autoplay=1')
