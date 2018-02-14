# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class JdPipeline(object):

    def __init__(self):
        self.file = open('jd.json','w')

    def process_item(self, item, spider):
        '保存获取的数据'
        dict_data = dict(item)
        data = json.dumps(dict_data,ensure_ascii=False) +',\n'
        self.file.write(data)
        return item

    def __del__(self):
        self.file.close()