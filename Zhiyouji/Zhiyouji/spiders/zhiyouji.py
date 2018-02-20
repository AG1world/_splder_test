# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Zhiyouji.items import ZhiyoujiItem

# 1. 导入类
from scrapy_redis.spiders import RedisCrawlSpider
# 2. 修改类的继承

class ZhiyoujiSpider(RedisCrawlSpider):
# class ZhiyoujiSpider(CrawlSpider):
    name = 'zhiyouji'
# 3. 注销允许的域和url
    # allowed_domains = ['jobui.com']
    # start_urls = ['http://www.jobui.com/cmp?area=%E5%85%A8%E5%9B%BD']
# 4. redis_key
    redis_key = 'zhiyouji'
# 5. 编写init,动态获取允许的域名
    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = list(filter(None, domain.split(',')))
        super(ZhiyoujiSpider, self).__init__(*args, **kwargs)

    rules = (
        Rule(LinkExtractor(allow=r'www.jobui.com/cmp\?area=%E5%85%A8%E5%9B%BD/'), callback='parse_item', follow=True),

        Rule(LinkExtractor(allow=r'/company/\d+/$'), callback='parse_item', follow=True),

    )

    def parse_item(self, response):
        '解析目标企业信息'
        # print(response.url)
        item = ZhiyoujiItem()

        item['data_source'] = response.url

        item['timestamp'] = time.time()

        item['company_name'] = response.xpath('//*[@id="companyH1"]/@data-companyname').extract_first()
        # 浏览次数
        item['views'] = response.xpath('/html/body/div[2]/div[1]/div/div[1]/div/div[2]/div[1]/text()').extract_first()
        if item['views'] :
            item['views'] = item['views'].split('人')[0].strip()

        item['slogan'] = response.xpath('//*[@id="companyH1"]/@data-companyname').extract_first()

        item['category'] = response.xpath('/html/body/div[2]/div[1]/div/div[1]/div[2]/p/text()').extract_first()

        item['industry'] = response.xpath('//*[@id="cmp-intro"]/div/div[2]/dl/dd[2]/a/text()').extract_first()

        item['desc'] = response.xpath('//*[@id="textShowMore"]/text()').extract_first()

        item['praise'] = response.xpath('//div[@class="swf-contA"]/div/h3/text()').extract_first()

        item['salary'] = response.xpath('/html/body/div[3]/div[1]/div[1]/div[3]/div[2]/div[1]/h3/text()').extract_first()

        item['address'] = response.xpath('//*[@class="dlli fs16"]/dd[1]/text()').extract_first()

        item['contact'] = response.xpath('//*[@class="j-shower1 dn"]/dd/text()').extract_first()
        if item['contact'] :
            item['contact'] = item['contact'].split('/')[0].strip()

        finance_info = []
        node_list = response.xpath('/html/body/div[3]/div[1]/div[1]/div[6]/ul/li')
        print('---------',node_list)
        # 遍历节点信息
        for node in node_list:
            temp = {}
            temp['time'] = node.xpath('./span[1]/text()').extract_first()
            temp['status'] = node.xpath('./h3/text()').extract_first()
            temp['sum'] = node.xpath('./span[2]/text()').extract_first()
            temp['investor'] = node.xpath('./span[3]/text()').extract_first()
            finance_info.append(temp)
        item['finance_info'] = finance_info
        print(item)
        yield item