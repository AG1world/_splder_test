# -*- coding: utf-8 -*-
import scrapy
from JD.items import JdItem

class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        # 获取大分类节点
        big_category = response.xpath('//*[@id="booksort"]/div[2]/dl/dt')
        # 获取小分类节点
        # small_category  =response.xpath('//*[@id="booksort"]/div[2]/dl/dt/following-sibling::*/em/a')
        for node in big_category[0]:
            item1 = {}
            item1['big_category'] = node.xpath('./a/text()').extract_first()
            item1['small_category'] = node.xpath('./following-sibling::*/em/a/text()').extract_first()
            item1['big_cate_link'] = 'http:'+ node.xpaht('./a/href').extract_first()
            # '//list.jd.com/1713-3258-3297.html'
            item1['small_cate_link'] ='http:' + node.xpath('./following-sibling::*/em/a/@href').extract_first()

            yield scrapy.Request(
                # 处理下一级url
                item1['small_category'],
                # 处理url的callback
                callback = 'detail_parse',
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

            item['price'] = node.xpath('')


# 注意:
    # meta传参中,item在大分类中创建item,不是不可以,本质都是字典,只是在多数替换少数更方便

    # price 怎么判断doc中没有,怎么通过js获取

    # 当复杂的js,怎么单独使用selenium获取price