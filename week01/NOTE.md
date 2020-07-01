## 1. The simplest Python scrapy example via requests
Assignment:
* To obtain the basic info of the top 250 movies from douban.
* The info includes: 
    * Name
    * Relase date
    * Score

Action:
requests v.s urlib: the APIs of requests is more elegant than that of urlib.
* The simplest flow:
    1. import requests
    2. request.get(target_url)
```
import requests

target_url = 'https://movie.douban.com/top250'

response = request.get(target_url)
```
It will probably fail under normal circunstances because the website detects an abnormal access.


Redefine "user-agent" can help us to imitate a browser to access the target website:

```
import requests

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

header = {'user-agent': user_agent}

target_url = 'https://movie.douban.com/top250'

response = requests.get(target_url, headers=header)
```
## 2. Use BeautifulSoup to parse the website
Assignment:
* To get all of the link w.r.t the name of the movies

Action:
* Analysis:
![](https://i.imgur.com/Q6fIKRS.png)
```
import requests
from bs4 import BeautifulSoup as bs

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

header = {'user-agent': user_agent}

target_url = 'https://movie.douban.com/top250'

response = requests.get(target_url, headers=header)

bs_info = bs(response.text, 'html.parser')

links = {}
for tag in bs_info.find_all('div', attrs={'class': 'hd'}):
    for a in tag.find_all('a'):
        '''
        links = {name_0: url_0,
                 name_1: url_1,
                 ...}
        '''
        links[a.find('span').text] = a.get('href')

```
## 3. Use XPath to parse the website
Pass
## 4. Implement page-turn actoin
