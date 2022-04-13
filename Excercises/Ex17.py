# Use the BeautifulSoup and requests Python packages
# to print out a list of all the article titles on the New York Times homepage.
# https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html
# requests: https://docs.python-requests.org/en/latest/user/quickstart/
# beautiful soup 4: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup

import requests
import bs4

html = requests.get("https://www.nytimes.com/")
# parsed = bs4(html,'html.parser')
print(html)
