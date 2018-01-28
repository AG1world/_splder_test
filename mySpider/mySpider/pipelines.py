# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#  写注意点：pipelines 中open_spider(),close_spider()俩个函数都是固定写法，必须，传参数需要spider


import json


class MyspiderPipeline(object):
    def open_spider(self,spider):
        '在开启爬虫时做相关处理，类似__init__'
        self.file = open('itcast.json','w')

    def process_item(self, item, spider):
        # 处理获取数据的格式问题
        #将item对象转换称字典形式
        dict_data = dict(item)
        str_data = json.dumps(dict_data,ensure_ascii=False) +',\n'
        self.file.write(str_data)

        #返回给引擎
        return item

    def close_spider(self,spider):
        '在爬虫结束之后调用'
        self.file.close()