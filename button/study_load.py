from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
import time

# A class to store all the details per Category
class Category:
  def __init__(self , name , urls):
    self.name  = 	name  
    self.urls = 	urls

def driverSetup():
    # Hides the browser window containing the search results
    co = webdriver.ChromeOptions()
    co.add_argument('headless')
    co.add_argument('window-size=1920x1080')
    co.add_argument("disable-gpu")
    # Path to webdriver
    serv = Service('./chromedriver')
    browser = webdriver.Chrome(service=serv, options=co)
    return browser

def loadUrls(browser):
    # Feel free to change the categories
    queries = ['anime', 'beach', 'window projector', 'chill rnb', 'white noise']
    hrefs = []
    categories = []
    print("✮*•̩̩͙✧•̩̩͙*˚✧*˚　Loading... Please wait　˚*✧˚*•̩̩͙✧•̩̩͙*˚✮")
    # For each category, save the the relevant YouTube video urls to the appropriate array
    for i in range(0, len(queries)):
        url = 'https://www.youtube.com/results?search_query=' + queries[i] + '+study+ambience'
        browser.get(url)
        # Parse html of webpage
        source = browser.page_source
        soup = BeautifulSoup(source,'html.parser')
        browser.get(url)
        # Find the YouTube urls of all the videos that resulted from each query
        hrefs = soup.find_all("a", class_="yt-simple-endpoint style-scope ytd-video-renderer")
        ytURLS = []
        for a in hrefs:
            ytURLS.append(a['href'])
        cat = Category(queries[i], ytURLS)
        categories.append(cat)
        #print(categories[i].urls)
        # Sleep for 2 seconds to make sure webpage has been thoroughly parsed
        time.sleep(2)
        print("╭➜ ๑ ̟ ̊" + queries[i] + " videos loaded.")

    return categories