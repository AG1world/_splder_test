# -*- coding:utf-8 -*-

# 爬取起点中文网的小说url

# 获取页面文字
# //*[@id="oneboolt"]/tbody/tr[2]/td[1]/div

# 下一章
# //*[@id="oneboolt"]/tbody/tr[5]/td[1]/span/a
import os

import re
from lxml import etree

import requests


class NovelSpi(object):
    def __init__(self):
        self.url = 'https://www.qisuu.com/du/24/24301/'
        self.headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0'
        }
    def get_response(self,url):
        response = requests.get(url,headers=self.headers)
        # print(response.content)
        with open('novel','w') as f :
            f.write(response.content.decode())
        return response.content

    def parse_list_url(self,content):
        '获取页面中推荐榜url'
        # 将页面转化称xml，生成element对象
        html = etree.HTML(content)
        # print(html)

        # 获取推荐榜书名ele对象列表
        xml_list = html.xpath('//*[@class="pc_list"]/ul/li/a')
        print(xml_list)
        # 遍历列表，得到书目名和url
        book_list = []
        for xml in xml_list:
            temp = {}
            text = xml.xpath('./text()')
            print('>>>>>>>>>>>',text)
            temp['text'] = xml.xpath('./text()')[0]if len(xml.xpath('./text()')) else None
            temp['url'] = 'https://www.qisuu.com/du/24/24301/' + xml.xpath('./@href')[0]if len(xml.xpath('./@href')) else None
            book_list.append(temp)
        # print(book_list)
        return book_list
    # def get_charpter_data(self,book_list):


    def save_data(self,book_list):


        for book in book_list:
            charpter_url = book['url']
            charpter_name = book['text']
            print(charpter_url)
            content = self.get_response(charpter_url)
# '<div  id="content1">
# “苟利国家生死以，岂因祸福避趋之。”林则徐悲壮的诗句在他的脑子里浮起，他决心向林则徐学习：力疾受命。
# <br />'
            html = etree.HTML(content)
            # print(html)
            # 获取推荐榜书名ele对象列表
            charpter_content = html.xpath('//*[@id="content1"]/text()')[0]
            charpter_content = re.sub('<br />',',\n',charpter_content)
            print(charpter_content)
            print(type(charpter_content))
        #     print(charpter_content)
            file_name = 'novel1' + os.sep + charpter_name
            # 路径通配符
            if not os.path.exists('novel1'):
                os.makedirs('novel1')
            with open(file_name,'w') as f:
                f.write(charpter_content)

    def run(self):
        url = self.url
        content =  self.get_response(url)
        book_list = self.parse_list_url(content)
        self.save_data(book_list)

if __name__ == '__main__':

    novel = NovelSpi()
    novel.run()