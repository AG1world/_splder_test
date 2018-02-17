# -*- coding: utf-8 -*-
import json

import scrapy
from JD.items import JdItem
# 1. 导入类
from scrapy_redis.spiders import RedisSpider

# 2. 修改继承的类

# class JdSpider(scrapy.Spider):
class JdSpider(RedisSpider):

    name = 'jd'
    # 3. 注销起始的url和允许的域名
    # allowed_domains = ['jd.com','3.cn']
    # start_urls = ['https://book.jd.com/booksort.html']

    # 4. 使用redis_key代替了起始url列表
    redis_key = 'book'

    # 5. 设置动态获取允许的域
    def __init__(self,*args,**kwargs):
        # 动态设置获取允许的域名列表
        domain = kwargs.pop('domain', '')
        # filter()生成一个过滤对象<迭代器>,第一个参数过滤的条件,第二个参数,带过滤列表
        # 为保证有效化一般在外部添加一个列表转化
        self.allowed_domains = list(filter(None, domain.split(',')))
        super(JdSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        # 获取大分类节点
        big_category = response.xpath('//*[@id="booksort"]/div[2]/dl/dt')
        # 获取小分类节点
        # small_category  =response.xpath('//*[@id="booksort"]/div[2]/dl/dt/following-sibling::*/em/a')
        for node in big_category[0:1]:
            item1 = {}
            item1['big_category'] = node.xpath('./a/text()').extract_first()
            item1['small_category'] = node.xpath('./following-sibling::*/em/a/text()').extract_first()
            item1['big_cate_link'] = 'http:'+ node.xpath('./a/@href').extract_first()
            # '//list.jd.com/1713-3258-3297.html'
            item1['small_cate_link'] ='https:' + node.xpath('./following-sibling::*/em/a/@href').extract_first()

            yield scrapy.Request(
                # 处理下一级url
                item1['small_cate_link'],
                # 处理url的callback
                callback = self.detail_parse,
                # meta 传参
                meta={'meta1':item1}
                )

    def detail_parse(self,response):
        item1 = response.meta['meta1']
        node_list = response.xpath('//*[@id="plist"]/ul/li/div')
        for node in node_list:
            item = JdItem()
            item['big_category'] = item1['big_category']
            item['small_category'] = item1['small_category']
            item['big_cate_link'] = item1['big_cate_link']
            item['small_cate_link'] = item1['small_cate_link']
            book_name = node.xpath('./div/a/em/text()').extract_first()
            if book_name is not None:

                item['book'] = book_name.strip()
            # else:
            #     # '//*[@id="plist"]/ul/li/div/div/div[2]/div[1]/div[3]/a/em
            #     book_name = node.xpath('./div/div[2]/div[1]/div[3]/a/em/text()').extract_first()
            #     item['book'] = book_name.strip()
            # 详情页面url
            # 作者
            item['author'] = node.xpath('./div[4]/span[1]/span/a/@title').extract_first()
            # 封面图片链接

            # 出版社
            # 出版时间

            # 价格，
            skuid = node.xpath('./@data-sku').extract_first()

            if skuid is not None:
                # price_link = 'https://p.3.cn/prices/mgets?type=1&skuIds=J_{},&pdbp=0&pdtk=&pdpin='.format(skuid)
                price_link = 'https://p.3.cn/prices/mgets?type=1&skuIds=J_'+skuid
                yield scrapy.Request(
                    # 处理下一级url
                    price_link,
                    # 处理url的callback
                    callback=self.price_parse,
                    # meta 传参
                    meta={'meta2': item}
                )
            # 获取下一页链接，并且做成请求发送个引擎
            # 拼接下一页url
            # small_cate_link = "https://list.jd.com/1713-3258-3297.html"
            # 'https://list.jd.com/list.html?cat=1713,3258,3297&page=2&sort=sort_rank_asc&trans=1&JL=6_0_0'
            # '/list.html?cat=1713,3258,3297&page=2&sort=sort%5Frank%5Fasc&trans=1&JL=6_0_0'

            # next_data = response.xpath('//*[@id="J_bottomPage"]/span[1]/a[10]/@href').extract()[0]
            # next_url = 'https://list.jd.com/' + next_data
            # # 判断是否到达最后一页
            # if next_url is  not None:
            #     # 没有到达最后一页就发送请求，模拟翻页
            #     yield scrapy.Request(next_url, callback=self.detail_parse)

    def price_parse(self,response):
        item = response.meta['meta2']
        json_data = json.loads(response.text)
        item['price'] = json_data[0]['op']

        yield item

