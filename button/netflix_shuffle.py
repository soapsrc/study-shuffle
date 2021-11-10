import webbrowser
import requests
from bs4 import BeautifulSoup
import random


# Pick a show
num = input("1 - How I Met Your Mother\n2 - Modern Family\n3 - Community\n4 - The Office\nEnter the number associated to the show you are planning to watch:\n")
if num == 1:    # HIMYM
    showName = "How I Met Your Mother"
    totalEpisodes = 208
elif num == 2:  # Modern Family
    showName = "Modern Family"
    totalEpisodes = 250
elif num == 3:  # Community
    showName = "Community"
    totalEpisodes = 110
else:           # The Office
    showName = "The Office"
    totalEpisodes = 201

# Select a random episode
randomEp = random.randint(1,totalEpisodes)
print("Playing " + showName + " episode: " + str(randomEp))

