# -*- coding:utf-8 -*-

#coding:utf-8
import requests
from lxml import etree
import json


class Qiushi(object):
    def __init__(self):
        self.url = 'https://www.qiushibaike.com/8hr/page/{}/'
        self.url_list = None
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        self.file = open('qiushi.json','w')

    def generate_url_list(self):
        self.url_list = [self.url.format(i) for i in range(1, 14)]

    def get_data(self, url):
        response = requests.get(url,headers=self.headers)
        return response.content

    def parse_data(self, data):
        # 创建element对象
        html = etree.HTML(data)

        # 定位出帖子节点列表
        node_list = html.xpath('//*[contains(@id,"qiushi_tag_")]')
        # print(len(node_list))

        # 构建存放返回数据的列表
        data_list = []

        # 遍历节点列表，从没一个节点中抽取数据
        for node in node_list:
            temp = dict()
            try:
                temp['user'] = node.xpath('./div[1]/a[2]/h2/text()')[0].strip()
                temp['link'] = 'https://www.qiushibaike.com' + node.xpath('./div[1]/a[2]/@href')[0]
                temp['age'] = node.xpath('./div[1]/div/text()')[0]
                temp['gender'] = node.xpath('./div[1]/div/@class')[0].split(' ')[-1].replace('Icon', '')
            except:
                temp['user'] = '匿名用户'
                temp['link'] = None
                temp['age'] = None
                temp['gender'] = None
            # 将数据加入数据列表
            data_list.append(temp)

        return data_list

    def save_data(self,data_list):
        for data in data_list:
            str_data = json.dumps(data,ensure_ascii=False)  + ',\n'
            self.file.write(str_data)

    def __del__(self):
        self.file.close()

    def run(self):
        # 构建url列表
        self.generate_url_list()
        # 构建请求头
        # 遍历url列表
        for url in self.url_list:
            # 发起请求获取响应
            data = self.get_data(url)
            # 解析数据
            data_list = self.parse_data(data)
            # 保存
            self.save_data(data_list)

if __name__ == '__main__':
    qiushi = Qiushi()
    qiushi.run()