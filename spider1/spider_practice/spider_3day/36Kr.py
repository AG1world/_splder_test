# -*- coding:utf-8 -*-
import json

import requests,re

# <script>var props=(.*?)</script>

url = 'http://36kr.com/'

class Kr36(object):
    def __init__(self):
        self.url = 'http://36kr.com'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        self.file = open('36kr.json','w')

    def get_data(self):
        '获取响应数据,二进制编码格式'
        resp = requests.get(self.url,headers =self.headers)
        return resp.content.decode()
    def parse_dict(self,content):
        '先正则匹配目标数据，解析数据'
        temp = re.findall('<script>var props=(.*?)</script>',content,re.DOTALL)[0]
        result = re.sub(",locationnal={.*" ,"", temp)
        with open('temp.json','w') as f:
            f.write(result)
        # 将json数据 转换成 python字典形式
        result_list = json.loads(result)["feedPostsLatest|post"]
        # 定义一个列表来装我想得到的信息（字典形式），在保存的时候遍历出字典元素，并转回json数据格式
        #python字典形式是不能直接存成文件
        data_list=[]
        for data in result_list:
            temp=dict()
            temp["title"]=data["title"]
            temp["cover"]=data["cover"]
            data_list.append(temp)
        return data_list


    def save_data(self,data_list):
        for data in data_list:
            data_json = json.dumps(data,ensure_ascii=False) + ', \n'
            self.file.write(data_json)

    def __del__(self):
        self.file.close()

    def run(self):
        # 获取请求头
        # 获取请求url
        # 获取响应数据
        # 解析数据
        # 保存数据
        content = self.get_data()
        data_list = self.parse_dict(content)
        self.save_data(data_list)


if __name__ == '__main__':
    kr36 = Kr36()
    kr36.run()
