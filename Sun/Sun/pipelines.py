# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.conf import settings
from pymongo import MongoClient

class SunPipeline(object):
    # pipeline用于处理从scrapy Engine中获取的item字段,保存数据操作
    #三个方法:
        # 保存成文件: 打开文件;处理文件,保存文件;关闭文件,close_spider()方法需要传self,spider["__del__()方法仅self"]

        # 保存到数据库:
        # 准备工作:导包,在settings中设置链接数据的port,hostname,dbnanme,colname
        # __init__方法创建链接数据的对象,db对象,col对象,
        # 写入集合中.返回item到引擎中
        # 关闭数据库

    # 保存到文件
    # def open_spider(self):
    #     self.file = open('阳光政务.json','w')
    #
    # def process_item(self, item, spider):
    #     str_data =json.dumps(dict(item),ensure_ascii=False) +',\n'
    #     self.file.write(str_data)
    #     return item
    #
    # def close_spider(self,spider):
    #     self.file.close()

    # 保存到数据库
    def __init__(self):
        # 数据库链接对象创建
        host = settings['MONGO_HOST']
        port = settings['MONGO_PORT']
        dbname = settings['MONGO_DBNAME']
        colname = settings['MONGO_COLNAME']

        self.client = MongoClient(host,port)
        self.db =self.client[dbname]
        self.col =self.db[colname]

    def process_item(self,item,spider):
        '插入数据'
        dict_data = dict(item)
        self.col.insert(dict_data)
        return item
    def __del__(self):
        '关闭数据库'
        self.client.close()