# -*- coding:utf-8 -*-

# 获取百度_贴吧的页面,并保存一个html文件
from sys import argv

import requests

# 函数版 获取新垣结衣贴吧页面
# 构建url
name = '新垣结衣'
page = 1
url = 'http://tieba.baidu.com/f?kw=%s&pn' % name +str(page*50)
# 构建请求头
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
# 构建参数

#发送请求获取响应
response = requests.get(url,headers=headers)
content = response.content
#保存源码
with open('新垣结衣1.html','wb') as f:
    f.write(content)

# 面向对象 获取不同贴吧,多页数文件

class TiebaFile(object):
    def __init__(self,name,num):

        self.name =name
        # 页数可以是多页,可以作为一个列表形式遍历 拼接
        self.base_url= 'http://tieba.baidu.com/f?kw={}&pn'.format(name)
        # self.page_list =[]
        # for i in range(page):
        #     url = self.base_url +str(i*50)
        #     self.page_list.append(url)

        # 构建url列表
        self.url_list = [self.base_url + str(i*50)for i in range(num)]
        # 构建headers
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
        print(self.name)
    # 获取请求响应
    def get_response(self,url):
        self.response = requests.get(url,headers =self.headers)
        return response.content
    # 存储数据
    def save_data(self,num,data):
        with open(self.name+'_'+str(num)+'.html','wb') as f:
            f.write(data)
    # 处理逻辑,传参
    def run(self):
        # 获取url
        for url in self.url_list:
            # 获取url请求
            data = self.get_response(url)
            num = self.url_list.index(url)
            self.save_data(num,data)

if __name__ == '__main__':
    name = argv[1]
    print(argv[1],argv[2])
    num = int(argv[2])
    tieba = TiebaFile(name,num)
    tieba.run()

#明确每个函数的执行,传入的参数,属于__init__属性加上 self.来调用,方法也是,
# 当方法中需要实参实.需要传入
