# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from items import ZhiyoujiItem

class ZhiyoujiSpider(CrawlSpider):
    name = 'zhiyouji'
    allowed_domains = ['jobui.com']
    start_urls = ['http://']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        '解析目标企业信息'
        item = ZhiyoujiItem()

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