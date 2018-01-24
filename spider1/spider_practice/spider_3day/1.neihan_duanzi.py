# -*- coding:utf-8 -*-
import json,re

import  requests

class Spider_neihan(object):
    def __init__(self):
        self.url = 'http://www.isocialkey.com/article/index.html'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
        }
    def get_response(self,url):
        response = requests.get(url,headers=self.headers)
        # 获取网页html数据
        content = response.content.decode()
        return content

    re_str = "< h3 > < a > (.*?) < / a > < / h3 >< div class ='desc' > 　(.*?)　　 < / div >"



    def parse_data(self,content):
        # print(self.content)
        with open('neihan','w')as f:
            f.write(content)
        result = re.findall()



    def run(self):
        # 构建url
        # 构建请求头
        # 发送请求，获取响应json数据
        self.get_response()
        self.get_data()
        # json转python数据

if __name__ == '__main__':
    neihan = Spider_neihan()
    neihan.run()

