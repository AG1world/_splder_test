# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

from scrapy.conf import settings
from pymongo import MongoClient

class DoubanPipeline(object):

        '保存到mongo中'
        # 三段式
        def __init__(self):
            dbname = settings['MONGO_DBNAME']
            port = settings['MONGO_PORT']
            colname = settings['MONGO_COLNAME']
            host = settings['MONGO_HOST']

            self.client = MongoClient(host,port)
            self.db = self.client[dbname]
            self.col = self.db[colname]

        def process_item(self, item, spider):
            '处理item对象中的字典数据'
            dict_data = dict(item)
            self.col.insert(dict_data)
            return item

        def __del__(self):
            self.client.close()


class DoubanPipeline_1(object):
    '保存到mongo中'

    # 三段式
    def __init__(self):
        self.file = open('douban250','w')
    def process_item(self, item, spider):
        '处理item对象中的字典数据'
        dict_data = dict(item)

        str_data = json.dumps(dict_data,ensure_ascii=False) +',\n'
        self.file.write(str_data)
        return item

    def __del__(self):
        self.file.close()
