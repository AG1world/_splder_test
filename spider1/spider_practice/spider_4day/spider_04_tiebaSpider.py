# -*- coding:utf-8 -*-
# 现在我们用XPath来做一个简单的爬虫，我们尝试爬取某个贴吧里的所有帖子
# 将该这个帖子里每个楼层发布的图片下载到本地。

# //*[@id="frs_list_pager"]/a[last()-1]/@href
# //*[@id="thread_list"]/li[@class ='j_thread_list clearfix']/div/div[2]/div[1]/div[1]/a
# '//cc/div[contains(@id,"content_")]/img'

import json
import os

from lxml import etree

import requests


class Tieba(object):
    def __init__(self,tie_name):
        self.name = tie_name
        self.url = 'http://tieba.baidu.com/f?kw={}'.format(self.name)
        # 使用低版本请求头获取 数据，不会被js屏蔽
        self.headers = {
            'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0'
        }

    def get_response(self,url):
        "获取所有响应页面"

        response = requests.get(url,headers=self.headers)
        with open('tieba_temp','wb') as f:
            f.write(response.content)
        return response.content

    def get_node_list(self,content):
        html = etree.HTML(content)
        # print(html)
        # 获取节点列表
        # node_list = html.xpath('//*[@id="thread_list"]/li[@class=" j_thread_list clearfix"]/div/div[2]/div[1]/div[1]/a')
        node_list = html.xpath('//*[@id="thread_list"]/li[@class=" j_thread_list clearfix"]/div/div[2]/div[1]/div[1]/a')
        # node_list = html.xpath('//*[@id="thread_list"]/li[2]/div/div[2]/div[1]/div[1]/a')

        # print(node_list)
        # 创建列表装填详细 text，href字典
        data_list = []
        for node in node_list:
            temp={}
            temp['text'] = node.xpath('./text()')[0]
            temp['url'] = 'http://tieba.baidu.com'+ node.xpath('./@href')[0]
            data_list.append(temp)
        # 提取下一页链接
        next_node = html.xpath('//*[@id="frs_list_pager"]/a[last()-1]/@href')
        next_url = 'http:' + next_node[0] if len(next_node) else None

        # print(next_url)
        return data_list ,next_url

    def get_detail_image_list(self,data):
        # 获取图片列表，从标题的标题的详情页
        html = etree.HTML(data)
        img_list = html.xpath('//cc/div[contains(@id,"content_")]/img/@src')
        # print(img_list)
        # 返回图片url列表
        return img_list

    def save_img(self,image_url_list):
        '保存存储的图片'
        # 判断当前文件下是否有image文件夹
        if not os.path.exists('huilicai_image'):
            os.makedirs('huilicai_image')
        for url in image_url_list:
            # 路径通配符
            print('>>>>>>>')
            file_name = 'huilicai_image' + os.sep + url.split('/')[-1]
            # print(file_name)
            data = self.get_response(url)
            with open(file_name,'wb') as f:
                f.write(data)


    def run(self):
        '实例化对象执行方法'
        next_url = self.url
        while next_url:
            print(next_url)
            # 获取列表页面的响应数据
            result = self.get_response(next_url)

            # 获取响应页面的数据列表和下一页的url
            data_list, next_url = self.get_node_list(result)
            # 遍历列表获取详情页的url
            for data in data_list:
                detail_url = data['url']
                content = self.get_response(detail_url)
                # print(content)
                # 从详情页中抽取图片url_list
                img_list = self.get_detail_image_list(content)
                # 从图片url响应中下载图片
                self.save_img(img_list)
                # 翻页

if __name__ == '__main__':
    tieba = Tieba('真野惠里菜吧')
    tieba.run()


