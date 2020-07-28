# Week02 作業
## 作業01
1. 下載 mysql docker
```shell=
bash run_docker.sh
```
2. 運行 mysql docker
```shell=
bash exec_docker.sh
```
3. 建立數據庫 movies，設定遠程訪問 movies
4. pymsql 連接數據庫，並創建 table maoyan
```shell=
cd hw1/maoyanmovie/
python mysql_connector.py
```
5. 使用 scrapy 爬取數據，並載入數據庫
```shell=
cd hw1
scrapy crawl maoyan
```
結果:![](https://i.imgur.com/sEWa2YY.png)

## 作業02
```shell=
cd hw2/
python login_shimo.py
```
結果:
print status_code: 204