# -*- coding: utf-8 -*-
import scrapy
import time

from AQI.items import AqiItem
# 导入redisspider类
from scrapy_redis.spiders import RedisSpider

# 修改继承类
class AqiSpider(RedisSpider):
# class AqiSpider(scrapy.Spider):
    name = 'aqi'
#注销其实url和域名
    # allowed_domains = ['aqistudy.cn']
    # start_urls = ['https://www.aqistudy.cn/historydata/']

    # 自定义动态获取域名
    def __init__(self,*args,**kwargs):

        domain = kwargs.pop('domain', '')
        self.allowed_domains = list(filter(None, domain.split(',')))
        super(AqiSpider, self).__init__(*args, **kwargs)

    # 编写redis_key
    redis_key = 'aqi'

    def parse(self, response):
        node_list = response.xpath('//div[@class="all"]/div[2]/ul/div[2]/li')

        for node in node_list[14:19]:
            temp = {}
            temp['city'] = node.xpath('./a/text()').extract_first()
            city_link = 'https://www.aqistudy.cn/historydata/' +  node.xpath('./a/@href').extract_first()
            yield scrapy.Request(
                city_link,
                meta={'meta1': temp},
                callback=self.month_parse
            )
    def month_parse(self,response):
        temp = response.meta['meta1']

        node_list = response.xpath('//div[@class="col-lg-3 col-md-4 col-sm-4 col-xs-12"]/div[2]/div[2]/ul/li')
        for node in node_list[14:19]:
            n = {}
            n['city'] = temp['city']
            day_link = 'https://www.aqistudy.cn/historydata/' + node.xpath('./a/@href').extract_first()
            yield scrapy.Request(
                day_link,
                meta={'meta2': n},
                callback=self.day_parse
            )
    # 由于数据都是js动态加载,只有通过selenium修改response获取动态加载后的网页数据
    # selenium使用修改是response,只有通过修改下载器中间件才行

    def day_parse(self,response):
        '每天空气质量状况'
        temp  = response.meta['meta2']
        node_list = response.xpath('//tr')

        for node in node_list:
            item = AqiItem()

            # # 城市
            item['city'] = temp['city']
            item['time'] = time.time()
            # # 日期
            # date = scrapy.Field()
            item['date'] = node.xpath('./td[1]/text()').extract_first()

            # # AQI
            item['aqi'] = node.xpath('./td[2]/text()').extract_first()


            # 质量等级
            item['quality_class'] = node.xpath('./td[3]/span/text()').extract_first()
            # PM2.5
            item['pm_2_5'] = node.xpath('./td[4]/text()').extract_first()
            # PM10
            item['pm_10'] = node.xpath('./td[5]/text()').extract_first()
            # SO2
            item['so2'] = node.xpath('./td[6]/text()').extract_first()
            # CO
            item['co'] = node.xpath('./td[7]/text()').extract_first()
            # NO2
            item['no2'] = node.xpath('./td[8]/text()').extract_first()
            # O3
            item['o3'] = node.xpath('./td[9]/text()').extract_first()

            yield item



