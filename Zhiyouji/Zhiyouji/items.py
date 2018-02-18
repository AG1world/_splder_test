# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhiyoujiItem(scrapy.Item):
    # define the fields for your item here like:
    data_source = scrapy.Field()

    timestamp = scrapy.Field()

    company_name = scrapy.Field()

    views = scrapy.Field()

    slogan = scrapy.Field()

    category = scrapy.Field()

    industry = scrapy.Field()

    desc = scrapy.Field()

    praise = scrapy.Field()

    salary = scrapy.Field()

    finance_info = scrapy.Field()

    address = scrapy.Field()

    contact = scrapy.Field()

