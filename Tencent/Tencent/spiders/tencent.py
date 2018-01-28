# -*- coding: utf-8 -*-
import scrapy

# spider 主要应用于处理response,获取item字段的相关数据和下一页需要跟进的url,
# 返回给spider engine
from Tencent.items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    # 怎么保证取到的数据没有出错,没有多写或者漏写
    def parse(self, response):
        node_list = response.xpath('//tr[@class="odd"]|//tr[@class="even"]')
        for node in node_list:
            item = TencentItem()
            item['name'] = node.xpath('./td[1]/a/text()').extract()[0]
            item['category'] = node.xpath('./td[2]/a/text()').extract_first()
            item['detail_link'] = 'https://hr.tencent.com' + node.xpath('./td[1]/a/@href').extract()[0]
            item['number'] = node.xpath('./td[3]/text()').extract()[0]
            item['address'] = node.xpath('./td[4]/text()').extract()[0]
            item['pub_date'] = node.xpath('./td[5]/text()').extract()[0]
            yield item

        # 获取下一页xpath
        next_url = 'https://hr.tencent.com/'+ response.xpath('//*[@id="next"]/@href').extract()[0]
        # 当下一页不为最后一页,将怎么做

        # if not next_url =='https://hr.tencent.com/javascript:;':
        if 'javascript:;'not in next_url:
            yield scrapy.Request(next_url, callback=self.parse)


 # 怎么保证取到的数据没有出错,没有多写或者漏写
 # 当下一页不为最后一页,将怎么做



