import requests
from user import (LOGIN_URL, EMAIL, PASSWORD, MOBILE)

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'

headers = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
    # 'cache-control': 'no-cache',
    'content-length': '71',
    'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
    'origin': 'https://shimo.im',
    # 'pragma': 'no-cache',
    'referer':
    'https://shimo.im/login?redirect_url=https%3A%2F%2Fshimo.im%2Fdashboard%2Fused',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': user_agent,
    'x-requested-with': 'XmlHttpRequest',
    'x-source': 'lizard-desktop',
}

from_data = {
    'email': EMAIL,
    'mobile': MOBILE,
    'password': PASSWORD,
}


if __name__ == '__main__':
    with requests.session() as sess:
        res = sess.post(url=LOGIN_URL, headers=headers, data=from_data)
        print('print status_code: ', res.status_code)
