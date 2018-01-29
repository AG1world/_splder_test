# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SunItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 编号,标题,投诉内容,处理状态
    num = scrapy.Field()
    title = scrapy.Field()
    comment = scrapy.Field()
    status = scrapy.Field()
    url = scrapy.Field()

