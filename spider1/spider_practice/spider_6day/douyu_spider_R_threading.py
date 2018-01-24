# https://www.douyu.com/directory/all
# https://www.douyu.com/gapi/rkc/directory/0_0/3
# 斗鱼爬取房间号，
import json
import os
import time
from queue import Queue
from threading import Thread

import requests

room_name='./a/div/p/span[1]'
visit_num = './a/div/p/span[2]'
image ='./a/span/img'
# data_rid ='./a/@href'[xpath]  ; data_rid ='./aattribute('href) selenium
category = './div/div/span'

node = '//*[@id="live-list-contentbox"]/li/a'


from lxml import etree

class DouYu(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        self.url = 'https://www.douyu.com/gapi/rkc/directory/0_0/{}'
        self.file = open('douyu666.json','w')
        self.url_queue = Queue()
        self.response_queue = Queue()
        self.data_queue = Queue()


    def url_list(self):
        url_list = [self.url.format(i)for i in range(1,78)]
        for url in url_list:
            # print(url,'111111')
            self.url_queue.put(url)


    def get_response(self):
        while True:
            time.sleep(3)
            url = self.url_queue.get()
            # print('222222')
            response = requests.get(url,headers=self.headers)
            assert response.status_code!='200','出错了'
            content = response.content.decode()

            self.response_queue.put(content)
            self.url_queue.task_done()


    def get_node_data(self):

        while True:
            content = self.response_queue.get()
            print(content, '333333')
            content_list =json.loads(content)['data']['rl']
            data_list = []
            for data in content_list:
                temp ={}
                temp['category']=data['c2name']
                temp['room_id']=data['rid']
                temp['name']=data['nn']
                temp['img']=data['rs1']
                data_list.append(temp)

            self.data_queue.put(data_list)
            self.response_queue.task_done()


    def save_data(self):
        while True:

            data_list = self.data_queue.get()
            # print( '4444444')
            for data in data_list:
                data_json = json.dumps(data,ensure_ascii=False) + ',\n'
                if not os.path.exists('douyu'):
                    os.mkdir('douyu')
                response = requests.get(data['img'])
                file_name = 'douyu'+os.sep + data['img'].split('/')[-1]
                with open(file_name,'wb') as f:
                     f.write(response.content)
                self.file.write(data_json)
            self.data_queue.task_done()


    def run(self):
        # 创建线程列表
        thread_list = []
        # 创建url线程
        t_url_thread = Thread(target=self.url_list)
        thread_list.append(t_url_thread)

        # 创建响应数据3个线程
        for t in range(3):
            t = Thread(target=self.get_response)
            thread_list.append(t)
        # 创建获取data数据三个线程
        for m in range(3):
            m = Thread(target=self.get_node_data)
            thread_list.append(m)

        #保存数据
        t_data_thread = Thread(target=self.save_data)
        thread_list.append(t_data_thread)

        # 开启保护，开启线程
        for t in thread_list:
            t.setDaemon(True)
            t.start()
        # 保证队列运行完后，主线程才会关闭
        for q in [self.url_queue,self.response_queue,self.data_queue]:
            q.join()
if __name__ == '__main__':
    douyu = DouYu()
    douyu.run()

"""
线程中target=函数名
t.setDaemon(True)
ajax请求的是json数据
response.statucode=='200'，是字符串
"""
