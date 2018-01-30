# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from Douban.items import DoubanItem


class Douban250Spider(CrawlSpider):
    name = 'douban250'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    rules = (
        # 'https://movie.douban.com/top250?start=0&filter='
        Rule(LinkExtractor(allow=r'\?start=\d+&filter='), callback='parse_item', follow=True),
        # 'https://movie.douban.com/top250?start=50&filter='
    )

    def parse_item(self, response):

        # spider 与crawl spider区别: 当数据在一页时,crawl spider 可以通过链接提取器来获取下一页的数据,
        # 当数据结构相同时,callback返回处理 'parse_item'方法
        # print(response.url)

        # 创建节点列表
        node_list = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        # print('---------------------')
        # print(len(node_list)
        # )
        for node in node_list:
            item = DoubanItem()
            item['film_name'] = node.xpath('./div/div[2]/div[1]/a/span[1]/text()').extract_first()
            # ''  导演: 弗兰克·德拉邦特 Frank Darabont   主演: 蒂姆·罗宾斯 Tim Robbins /...    ''

            # ''              1994 / 美国 / 犯罪 剧情     ''
            temp = node.xpath('./div/div[2]/div[2]/p[1]/text()').extract()
            # print(temp)

            item['direc_name'] = (temp[0].split(': ')[1]).split('   ')[0]
            # print('---------------------')
            # print(direc_name)
            try:
                item['protagonist'] = (temp[0].split(': ')[2]).split(' /')[0]
            except Exception as e:
                protagonist='nodisplay'
            # print('---------------------')
            # print(protagonist)

            item['score'] = node.xpath('./div/div[2]/div[2]/div/span[2]/text()').extract_first()
            # print('---------------------')
            # print(score)
            item['vote'] = node.xpath('./div/div[2]/div[2]/div/span[4]/text()').extract_first()
            # print('---------------------')
            # print(vote)
            item['comment'] = node.xpath('./div/div[2]/div[2]/p[2]/span/text()').extract_first()
            # print('---------------------')
            # print(comment)
            item['num'] = node.xpath('./div/div[1]/em/text()').extract_first()
            # print('---------------------')
            # print(num)
            item['publish_date'] = temp[-1].split('/')[0].strip()
            # print('---------------------')
            # print(publish_date)
            item['country'] = temp[-1].split('/')[1].strip()
            # print('---------------------')
            # print(country)
            print(item)
            yield item

# 注意: 1.网络问题,链接不上;2. 获取或者提取链接时,?记得带上
