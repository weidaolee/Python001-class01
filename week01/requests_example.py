import requests

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

header = {'user-agent': user_agent}

target_url = 'https://movie.douban.com/top250'

response = requests.get(target_url, headers=header)

