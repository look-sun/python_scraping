import re
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def get_title(url):
    try:
        html  = urlopen(url)
    except HTTPError as e:
        # Show why dose error pop-up
        print(e)
        return None

    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        # Show why dose error pop-up
        return None

    # Title has been return if code did not make error
    return title

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
images = bs.findAll('img', {'src': re.compile('../img/gifts/img.*.jpg')})
for image in images:
    print(image)

