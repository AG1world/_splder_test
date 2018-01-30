# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # 电影名
    film_name = scrapy.Field()
    # 导演名
    direc_name = scrapy.Field()
    # 主演名
    protagonist = scrapy.Field()
    # 分数
    score = scrapy.Field()
    # 投票数
    vote = scrapy.Field()
    # 简评
    comment = scrapy.Field()
    # 排序名次
    num = scrapy.Field()
    # 发行时间
    publish_date = scrapy.Field()
    #出版国家
    country = scrapy.Field()

