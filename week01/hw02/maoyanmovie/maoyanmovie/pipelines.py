# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
import re
import pandas as pd


class MaoyanmoviePipeline:
    def process_item(self, item, spider):
        data = {
            'Name': [item['Name'].extract_first()],
            'Type': [' '.join([t.strip() for t in item['Type'].extract()])],
            'Date': [
                re.search(r'\d{4}-\d{2}-\d{2}',
                          item['Date'].extract_first()).group()
            ]
        }

        keys = ['Name', 'Type', 'Date']

        save_path = './scrapy_xpath.csv'
        if not os.path.exists(save_path):
            with open(save_path, 'w') as f:
                f.write(','.join(keys) + '\n')

        row = pd.DataFrame(data=data, columns=keys)
        row.to_csv(save_path, mode='a', index=False, header=False)

        return data
