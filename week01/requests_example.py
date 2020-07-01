import time
import requests

from bs4 import BeautifulSoup as bs

target_url = 'https://movie.douban.com/top250'

urls = [f'{target_url}?start={p * 25}&filter=' for p in range(10)]

def get_name_url(target_url):

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

    header = {'user-agent': user_agent}

    response = requests.get(target_url, headers=header)

    bs_info = bs(response.text, 'html.parser')

    links = {}
    # find all tags which have attributes and class == hd
    for tag in bs_info.find_all('div', attrs={'class': 'hd'}):
        for a in tag.find_all('a'):
            '''
            links = {name_0: url_0,
                     name_1: url_1,
                     ...}
            '''
            links[a.find('span').text] = a.get('href')
    return links

res = {}

for u in urls:
    res.update(get_name_url(u))
    time.sleep(5)

