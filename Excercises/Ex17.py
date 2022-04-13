# Use the BeautifulSoup and requests Python packages
# to print out a list of all the article titles on the New York Times homepage.
# https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html

import requests
import bs4 as soup

r = requests.get("https://www.nytimes.com/")