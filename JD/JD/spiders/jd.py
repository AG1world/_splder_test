# -*- coding: utf-8 -*-
import json

import scrapy
from JD.items import JdItem

class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com','3.cn']
    start_urls = ['https://book.jd.com/booksort.html']

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



# Questions:


    # meta传参中,item在大分类中创建item,不是不可以,本质都是字典,只是在多数替换少数更方便

    # price 怎么判断 network 中没有,怎么通过js获取
        # 首先验证　书写的ｘｐａｔｈ是否可以获取页面中的数据
        # 不行: 首先将xpath粘在页面中检测是否能获取
        # 不行: 将 获取关键字 粘贴在allfiles find 中查找
        # 无: 则是js获取
        # js: 分类- js动态请求另一个网页数据,获取url,得到目标数据
                #   大量js计算,短时间无法破解,通过自动化测试工具获取

    # 获取相邻节点中的子节点
        # /follow-sibiling::*[0或者不写]

    # 当复杂的js,怎么单独使用selenium获取price

    # 测试时应该指选取少量来验证ｘｐａｔｈ是否书写正确，否则，项目没有运行ｉｐ就直接被封掉
    # 节点列表选择器不能以［０］切片，却可以使用［０：１］来切片

    # 回调函数什么时候调用使用函数名的字符串，什么适合调用类中的函数（self.callfunc）
        #    １． spider  使用的回调函数应该是调用类中的方法
        #　　２．　crawl spider 应该使用是的字符串

    #  获取下一页数据？？？？
        # 获取下一页xpath，再拼接下一页url，并通过scrapy.request来调用函数,及参数的传递
    # 怎么校对页面少的节点
        # 通过xpath再次尝试在页面中获取的节点个数
        #　'//*[@id="plist"]/ul/li/div/div[3]/a/em'

    # 服务器域名与页面访问地址等关系区别
    