import requests
from bs4 import BeautifulSoup
import time
import urllib.request

resp = requests.get('https://www.instagram.com/canonkorea/').text
soup = BeautifulSoup(resp, 'html.parser')
titles = soup.select('#react-root > section > main > div > div._2z6nI > article > div:nth-child(1) > div > div:nth-child(1)')


# urls = titles.select('')

# for url in urls:
#     i =+ 1
#     urllib.request.urlretrieve(url, (i) + ".jpg")