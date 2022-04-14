# Use the BeautifulSoup and requests Python packages
# to print out a list of all the article titles on the New York Times homepage.
# https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html
# requests: https://docs.python-requests.org/en/latest/user/quickstart/
# beautiful soup 4: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup

import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.nytimes.com/")
html = html.text
soup = BeautifulSoup(html,'html.parser')
titles = soup.find_all('h3')
for t in titles:
    print(t.text)