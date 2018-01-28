# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

from Tencent.items import TencentItemPro,TencentItem


class TencentPipeline(object):
    # def open_spider(self, spider):
    #     '在开启爬虫时做相关处理，类似__init__'
    #     self.file = open('itcast.json', 'w')

    def __init__(self):
        self.file = open('tencent.json','w')

    def process_item(self, item, spider):
        if isinstance(item, TencentItem):
            # item just 是一个对象,dict(item)转字典
            str_data = json.dumps(dict(item), ensure_ascii=False) + ',\n'
            self.file.write(str_data)
        return item

    def close_spider(self, spider):
        self.file.close()

class TencentPipelinePro(object):
    # def open_spider(self, spider):
    #     '在开启爬虫时做相关处理，类似__init__'
    #     self.file = open('itcast.json', 'w')

    def __init__(self):
        self.file = open('tencentpro.json','w')

    def process_item(self, item, spider):
        if  isinstance(item,TencentItemPro):
            # item just 是一个对象,dict(item)转字典
            str_data  = json.dumps(dict(item),ensure_ascii=False) + ',\n'
            self.file.write(str_data)
        # 返回给引擎
        return item

    def close_spider(self, spider):
        self.file.close()
