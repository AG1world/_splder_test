# -*- coding: utf-8 -*-

# 人人网实验于提交post请求,模拟正常登录账号

import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren2'
    allowed_domains = ['renren.com']
    # start_urls = ['http://www.renren.com/PLogin.do']
    start_urls = ['http://www.renren.com']


    #分析: 重写start_requests(),修改method,提交的数据

    #1. post请求:url,提交数据

    # 通过parse()方法,返回到FormReqest.from_response(response,formdata,callback)
    # 怎么看出post请求方式
    def parse(self, response):
        post_data = {
            'email':'17173805860',
            'password':'1qaz@WSX3edc',
        }
        yield scrapy.FormRequest.from_response(
            response,
            formdata=post_data,
            callback=self.parse_login
        )

    def parse_login(self,response):
        with open('renre_form.html','wb') as f:
            f.write(response.body)
    # 通过parse()方法,返回到FormReqest.from_response(response,formdata,callback)
    # 怎么看出