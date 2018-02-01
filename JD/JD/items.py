# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdItem(scrapy.Item):
    # define the fields for your item here like:
    # 需求: 抓取京东图书信息

    # 目标字段:
    # 书名，大分类，小分类，封面图片链接，详情页面url，作者，出版社，出版时间，价格，大分类页面url，小分类页面url
    # url:     https://book.jd.com/booksort.html
    # 书名
    book = scrapy.Field()
    # 大分类
    big_category = scrapy.Field()
    # 小分类
    small_category = scrapy.Field()
    # 大分类页面ur
    big_cate_link = scrapy.Field()
    # 小分类页面url
    small_cate_link = scrapy.Field()
    # 详情页面url
    detail_link = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 封面图片链接
    img_link= scrapy.Field()
    # 价格，
    price = scrapy.Field()
    # 出版社
    publisher = scrapy.Field()
    # 出版时间，
    pub_date = scrapy.Field()

