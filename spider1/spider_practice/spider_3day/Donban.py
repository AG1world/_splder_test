# -*- coding:utf-8 -*-

import requests
import json

class Douban(object):
    def __init__(self):
        self.url='https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?start={}&count=50'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Mobile Safari/537.36'
        }
        # 构建url，start从a+50开始
        self.n = 0
        self.file = open('douban.json','w')

    def get_resp(self,url):
        """获取response.content.decode()"""
        response = requests.get(url,headers=self.headers)
        content = response.content.decode()
        return content

    def get_parse_data(self,content):
        """获取目标数据,将json字符串转成字典"""
        dict_data = json.loads(content)
        tv_list = dict_data['subject_collection_items']
        # 构建存放数据的列表
        result_list=[]
        for tv in tv_list:
            temp={}
            temp['id']=tv['id']
            temp['rating']=tv['rating']
            temp['title']=tv['title']
            temp['url']=tv['url']
            result_list.append(temp)
        return result_list

    def save_data(self,data_list):
        """将tv信息字典组成的列表写入文件"""

        for data in data_list:
            # 将字典转化成json字符串才可以写入文件
            str_data = json.dumps(data,ensure_ascii=False) +',\n'
            self.file.write(str_data)
    def __del__(self):
        """关闭文件"""
        self.file.close()


    def run(self):
        while True:
            # 构建url
            url = self.url.format(self.n)
            print(url)
            # 构建headers
            # 获取响应结果
            content = self.get_resp(url)
            # 获取目标数据
            data_list = self.get_parse_data(content)
            # 保存数据
            self.save_data(data_list)
            # 累加 n 值，循环停止的条件
            self.n +=50
            if len(data_list) is 0:
                break


if __name__ == '__main__':
    douban=Douban()
    douban.run()