# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
import re
import pymysql
import pandas as pd
from maoyanmovie.mysql_connector import ConnDB
from maoyanmovie.user import dbInfo


class MaoyanmoviePipeline:
    def __init__(self):
        self.keys = ['Name', 'Type', 'Date']
        self.data = {}

    def process_item(self, item, spider):
        self.data = {
            'Name': [item['Name'].extract_first()],
            'Type': [' '.join([t.strip() for t in item['Type'].extract()])],
            'Date': [
                re.search(r'\d{4}-\d{2}-\d{2}',
                          item['Date'].extract_first()).group()
            ]
        }

        save_path = './scrapy_xpath.csv'
        self._save_csv(save_path)
        self._insert2mysql(dbInfo)

    def _save_csv(self, save_path: ''):

        if not os.path.exists(save_path):
            with open(save_path, 'w') as f:
                f.write(','.join(self.keys) + '\n')

        row = pd.DataFrame(data=self.data, columns=self.keys)
        row.to_csv(save_path, mode='a', index=False, header=False)

    def _insert2mysql(self, dbInfo):
        db = ConnDB(dbInfo)
        db.insert(self.data)


