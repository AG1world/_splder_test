# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 明确目标，爬去数据对应字段名

    # 职位名
    name = scrapy.Field()
    #详情url
    detail_link = scrapy.Field()
    # 职位类型
    category = scrapy.Field()
    # 人数
    number = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 发布日期
    pub_date = scrapy.Field()

class TencentItemPro(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 明确目标，爬去数据对应字段名

    # 职位名
    name = scrapy.Field()
    #详情url
    detail_link = scrapy.Field()
    # 职位类型
    category = scrapy.Field()
    # 人数
    number = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 发布日期
    pub_date = scrapy.Field()
    # 职位职责
    duty = scrapy.Field()
    # 工作要求
    require = scrapy.Field()