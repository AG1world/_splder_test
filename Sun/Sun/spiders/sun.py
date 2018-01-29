# -*- coding: utf-8 -*-

from Sun.items import SunItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SunSpider(CrawlSpider):
    name = 'sun'
    # 编辑允许的域名
    allowed_domains = ['sun0769.com']
    # 编辑起始url
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4']
    # 实例化Rule,allow:提取目标页面的url关键词(唯一),callback:使用回调函数名字字符串形式,follow指开启链接器提取url中页面数据
    rules = (
        # 列表页面数据: http://wz.sun0769.com/index.php/question/questionType?type=4
        Rule(LinkExtractor(allow=r'/question/questionType'), follow=True),
        # http://wz.sun0769.com/html/question/201801/359884.shtml
        Rule(LinkExtractor(allow=r'/question/\d+?/\d+?\.shtml'), callback='parse_item')
    )

    def parse_item(self, response):
        # 提取数据item字段,验证提取器是否有效
        # print('!!!!!!!!',response.url)

        # 创建item实例
        item = SunItem()
        item['url'] = response.url
        #  提问：机车铁牌，居住证  编号:177512
        temp=response.xpath('//*[@class="pagecenter p3"]/div[1]/div[1]/div[1]/strong/text()').extract()[0].split('\xa0\xa0')
        # print(temp,'>>>>>>>>>>>')
        # [' 提问：大片美市场公交站对面天天晚上施工噪音大', '编号:177496', '']
        item['title'] =temp[0].split('：')[1]
        item['num'] =(temp[1].split(':'))[1]

        # 分无图://*[@class="c1 text14_2"]/text()   有图://*[@class="contentext"]//text()
        # 切有俩个列表,怎么拼接
        item['comment'] = ''.join(response.xpath('//*[@class="c1 text14_2"]/text()').extract())
        if len(item['comment'].strip())==0:
            item['comment'] = ''.join(i.strip()for i in response.xpath('//*[@class="contentext"]//text()').extract())
            print('----------------------------------------')

        print(item['comment'])
        # item['comment'] = response.xpath('//*[@class="contentext"]//text()').extract()
        # print(item['title'],'------------')
        # print(item['num'],'111111111')
        # 可获取
        item['status'] = response.xpath('//span[@class="qgrn"]/text()').extract_first()
        yield item

#  注意:当数据使用xpath获取到的是result为1,但是又不显示字符,使用strip()去除,并使用len()==0,来作为俩者的分割条件
    # 在浏览器中的空格等转移字符,都需要按照python中的  空格或者换行符来处理
    # 注意浏览器上的不同字符,一律粘贴,切勿手打,格式编码不一样
    # 现阶段为练习阶段,积累经验,多用点耐心,多验证,打印