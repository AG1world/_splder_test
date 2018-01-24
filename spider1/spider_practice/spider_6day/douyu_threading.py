# -*- coding:utf-8 -*-

# https://www.douyu.com/directory/all
# https://www.douyu.com/gapi/rkc/directory/0_0/2   ajax请求的网址
#  selenium 多线程 ToDO 待完成
# 斗鱼爬取房间号，
import json
import threading
import time
from queue import Queue

room_name='./a/div/p/span[1]'
visit_num = './a/div/p/span[2]'
image ='./a/span/img'
# data_rid ='./a/@href'[xpath]  ; data_rid ='./aattribute('href) selenium
category = './div/div/span'

node = '//*[@id="live-list-contentbox"]/li/a'


from selenium import webdriver

class DouYu(object):
    def __init__(self,url):

        self.driver = webdriver.Chrome()
        # 请求首页，通过浏览器打开制定首页
        self.driver.get(url)
        self.file = open('douyu_threading.json','w')
        # self.url_queue = Queue()
        self.data_queue = Queue()
        self.save_queue = Queue()

    def get_url(self):
        # 现在获取10页数据，开启



        # while True:
            # time.sleep(3)
            # if self.driver.find_elements_by_xpath('//*[@id="J-pager"]/a[11]'):
            #     self.driver.find_elements_by_xpath('//*[@id="J-pager"]/a[11]').click()
            #     print('1111')


    def get_data(self):
        time.sleep(3)
        el_list = self.driver.find_elements_by_xpath('//*[@id="live-list-contentbox"]/li')
        print(el_list)
        data_list = []
        for el in el_list:
            temp = {}
            temp['room_name'] = el.find_element_by_xpath('./a/div/p/span[1]').text
            temp['visit_num'] = el.find_element_by_xpath('./a/div/p/span[2]').text
            temp['image'] = el.find_element_by_xpath('./a/span/img').get_attribute('data-original')
            temp['category'] = el.find_element_by_xpath('./a/div/div/span').text
            print(temp)
            data_list.append(temp)
        # return data_list
        self.data_queue.put(data_list)


    def save_data(self):
        while True:
            data_list=self.data_queue.get()
            for data in data_list:
                data_json = json.dumps(data,ensure_ascii=False) + ',\n'
                self.file.write(data_json)
            self.data_queue.task_done()




    def run(self):

        # 创建存储线程列表
        thread_list = list()

        # 创建url生成线程
        t_list_url = threading.Thread(target=self.get_url)
        thread_list.append(t_list_url)

        # 创建获取数据的3个线程
        for i in range(3):
            t_list_response = threading.Thread(target=self.get_data)
            thread_list.append(t_list_response)

        # 创建保存数据 线程
        t_save_data = threading.Thread(target=self.save_data)
        thread_list.append(t_save_data)
        # 开启守护线程,当主线程完成时，子进程就会被收回
        # 队列 q.jion()保证线程中的队列完成后，主线程才会结束
        # 保证子线程在循环时，当队列完成后就会停止主线程，并回收子线程【默认主线程完成，子线程不停止】
        for t in thread_list:
            t.setDaemon(True)
            t.start()
        # 主线程结束是在队列完成之后
        for q in [ self.save_queue, self.data_queue]:
            q.join()

if __name__ == '__main__':
    douyu = DouYu()
    douyu.run()


                # 请求首页，通过浏览器打开指定首页
        #通driver打开首页，并且通过xpath定位节点列表
        # data_list  = self.get_data()
        # 遍历节点列表，将每个节点数据存在响应的字典中，再通过新列表装填
        # 遍历新列表，得到字典数据，在dumps ，转化json数据，存储
        #运行实例化方法，得到一整页面后，通过定位到下一页节点，循环获取，当获取不下一页节点，即可终止程序
        # self.save_data(data_list)

        # '<a href="#" class="shark-pager-next">下一页</a>'
        # 下一页请求只能通过ajaxk出发
        # xpath   == //*[@id="J-pager"]/a[11]

        # while self.driver.find_element_by_xpath ('//*[@id="J-pager"]/a[11]'):
        #     time.sleep(3)
        #     self.driver.find_element_by_xpath('//*[@id="J-pager"]/a[last()-1]').click()
        #     # time.sleep(3)
        #     data_list = self.get_data()
        #     self.save_data(data_list)




    # def __del__(self):
    #     self.file.close()

