# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        '解析数据，框架和xpath找不同'
        # 存放老师信息的集合
        # items = []
        for temp in response.xpath("//div[@class='li_txt']"):
            item = ItcastItem()

            name = temp.xpath("h3/text()").extract()
            level = temp.xpath("h4/text()").extract()
            info = temp.xpath("p/text()").extract()

            item['name'] = name[0]
            item['level'] = level[0]
            item['info'] = info[0]

            # items.append(item)
            # 使用yield用来返回数据，并返回下一页url
            yield item
        # return items
        # yield 'http://wwww.baidu.com'