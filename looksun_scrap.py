import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random


random.seed(datetime.datetime.now())


def get_wikipedia(article_url):
    html = urlopen(f'http://en.wikipedia.org/wiki{article_url}')
    bs = BeautifulSoup(html, 'html.parser')
    # ^(/wiki/) url must start with /wiki/
    # ((?!:).)*$ url must have some chars without : And this char is last one
    return bs.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))


links = get_wikipedia("Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    link = get_wikipedia(newArticle)

