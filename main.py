from urllib.error import HTTPError, URLError
from urllib.request import (urlopen)
from bs4 import BeautifulSoup as BS4

def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    except URLError as e:
        print('The Server Couldn\'t be Found!', e)

    try:
        bs = BS4(html.read(), 'html.parser')
    except AttributeError as e:
        return None
    return bs

title = get_title('https://cse.snu.ac.kr/node/29041').body.table
# title = get_title('https://instagram.com/')
print(title)

