import re
import requests
import pandas as pd

from bs4 import BeautifulSoup as bs


def crawl(parser: object, url: '', user_agent: '', cookie: '') -> object:
    header = {'user-agent': user_agent, 'cookie': cookie}
    response = requests.get(url, verify=True, headers=header)

    return parser(response)


def get_target_urls(response: requests.Response) -> []:
    bs_info = bs(response.text, 'html.parser')
    top_10_info = bs_info.find_all(
        'div', attrs={'class': 'channel-detail movie-item-title'})[:10]
    
    target_urls = []
    for tag in top_10_info:
        for a_tag in tag.find_all('a'):
            href = a_tag.get('href')
            target_urls.append(f'https://maoyan.com{href}')

    return target_urls


def get_movie_info(response: requests.Response) -> {}:
    bs_info = bs(response.text, 'lxml')
    tag = bs_info.find_all('div', attrs={'class': 'movie-brief-container'})[0]

    name = tag.find('h1').text
    info = tag.find('ul').find_all('li')  # [type:[], loc, date]

    movie_info = {
        'Name': name,
        'Type': info[0].text.strip().replace(' \n ', ' '),
        'Date': re.search(r'\d{4}-\d{2}-\d{2}', info[-1].text).group()
    }

    return movie_info


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

cookie = '__mta=214726952.1593850009964.1593880254253.1593880344744.12; uuid_n_v=v1; uuid=509181C0BDCD11EAB5685D560D8487BBFF7A2266D34C4BB8B540F427E88AC6EC; _csrf=83e892560b2dfc8e596a40d5ef988c4c8b7d04bb8a88c012644154829b00efee; mojo-uuid=fb15aa44a9d0606a427d2666a03b10e6; _lxsdk_cuid=17318dd18a6c8-0c688aa49ea96b-4353760-144000-17318dd18a6c8; _lxsdk=509181C0BDCD11EAB5685D560D8487BBFF7A2266D34C4BB8B540F427E88AC6EC; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593850009,1593850369,1593867642; mojo-session-id={"id":"b8dab81dec451d3ffbe805c655348dca","time":1593880095631}; mojo-trace-id=6; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593880452; __mta=214726952.1593850009964.1593880344744.1593880452848.13; _lxsdk_s=1731aa81eba-b7b-0f4-dd1%7C%7C12'

start_url = 'https://maoyan.com/films?showType=3&sortId=1'

target_urls = crawl(get_target_urls, start_url, user_agent, cookie)

res = [crawl(get_movie_info, url, user_agent, cookie) for url in target_urls]

table = pd.DataFrame(data=res, columns=['Name', 'Type', 'Date'])
table.to_csv('req_bs4.csv', index=False)
