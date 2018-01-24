# -*- coding:utf-8 -*-

#coding:utf-8
import threading
from queue import Queue

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
        self.file = open('qiushi_threding.json','w')
        # 创建线程队列,处理url response data
        self.url_queue = Queue()
        self.response_queue = Queue()
        self.data_queue = Queue()




    def generate_url_list(self):
        for i in range(1, 14):
            self.url_queue.put(self.url.format(i))

    def get_data(self):
        while True:
            url = self.url_queue.get()
            print('正在获取url')

            response = requests.get(url,headers=self.headers)
            #保证多线程获取完全，打印response.status_code
            if response.status_code ==503:
                self.url_queue.put(url)
            else:
                self.response_queue.put(response)

            self.url_queue.task_done()

    def parse_data(self):
        while True:

            data = self.response_queue.get()
            print('正在解析数据')
            # 创建element对象
            html = etree.HTML(data.content)

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

            self.data_queue.put(data_list)
        #保证队列get获取完成
            self.response_queue.task_done()

    def save_data(self):
        while True:
            data_list = self.data_queue.get()
            print('存储数据')
            for data in data_list:
                str_data = json.dumps(data,ensure_ascii=False)  + ',\n'
                self.file.write(str_data)
            self.data_queue.task_done()

    def __del__(self):
        self.file.close()

    def run(self):

        # 创建存储线程列表
        thread_list = list()


        # 创建url生成线程
        t_list_url = threading.Thread(target=self.generate_url_list)
        thread_list.append(t_list_url)

        # 创建获取数据的3个线程
        for i in range(3):
            t_list_response = threading.Thread(target=self.get_data)
            thread_list.append(t_list_response)

        # 创建解析数据的3个线程
        for i in range(3):
            t_parse_data = threading.Thread(target=self.parse_data)
            thread_list.append(t_parse_data)

        # 创建保存数据 线程
        t_save_data = threading.Thread(target=self.save_data)
        thread_list.append(t_save_data)
        # 开启守护线程,当主线程完成时，子进程就会被收回
        #队列 q.jion()保证线程中的队列完成后，主线程才会结束
        #保证子线程在循环时，当队列完成后就会停止主线程，并回收子线程【默认主线程完成，子线程不停止】
        for t in thread_list:
            t.setDaemon(True)
            t.start()
        #主线程结束是在队列完成之后
        for q in [self.url_queue,self.response_queue,  self.data_queue]:
            q.join()


if __name__ == '__main__':
    qiushi = Qiushi()
    qiushi.run()

