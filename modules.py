def get_p(__search__):
    import urllib
    import pandas as pd
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from time import sleep
    # __search__ = '오버핏'  # input('검색어를 입력하세요 : ')
    search = urllib.parse.quote(__search__)
    url = 'https://www.instagram.com/explore/tags/' + str(search) + '/'

    __time__ = 8

    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(url)
    sleep(__time__)

    SCROLL_PAUSE_TIME = 1.0

    csvtext = []

    while True:
        pageString = driver.page_source
        bsObj = BeautifulSoup(pageString, 'lxml')

        for link1 in bsObj.find_all(name='div', attrs={"class": "Nnq7C weEfm"}):
            title = link1.select('a')[0]
            real = title.attrs['href']
            print(real)
            csvtext.append(real)
            title = link1.select('a')[1]
            real = title.attrs['href']
            print(real)
            csvtext.append(real)
            title = link1.select('a')[2]
            real = title.attrs['href']
            print(real)
            csvtext.append(real)

        last_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(SCROLL_PAUSE_TIME)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            else:
                last_height = new_height
                continue

    data = pd.DataFrame(csvtext)
    data.to_csv(__search__+'.insta'+'.txt', encoding='utf-8')

    driver.close()
    # 코드의 일부는 https://yeowool0217.tistory.com/552 여기서 따옴
    return 'end'


def get_img(p_list):
    for p in p_list:
        print(p)
    return 'end'
