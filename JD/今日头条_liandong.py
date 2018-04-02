
# -*- coding: utf-8 -*-
'''
设计一个模块用于实现爬取今日头条的信息
'''

# 创建一个类用于获得今日头条的信息
import json
import random

import requests
import time
from selenium import webdriver


class TouTiao(object):
    # 初始化的操作
    def __init__(self):
        # 构造请求的url
        self.web_index_url = 'https://www.toutiao.com/api/pc/feed/?min_behot_time=0&_signature=SLgwDAAAEi6G07beICicIEi4MB'
        # 构造后续页面信息的请求url
        self.web_after_url = 'https://www.toutiao.com/api/pc/feed/?max_behot_time={}&_signature={}'
        # 获得签名的url
        self.sign_url = 'https://s3a.pstatp.com/toutiao/static/js/page/index_node/index.0d66f4332f4f1b5d5d87.js'
        # 构造请求头
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        # 构造请求信息
        self.params = {

        }
        # 配置用于保存数据的本地文件
        self.file = open('toutiao.txt', 'w')
        self.proxy_list = [
            '116.199.2.208:82',
            '125.117.134.117:9000',
            '120.25.164.134:8118',
            '116.199.115.79:82',
            '59.110.221.78:80',
            '117.78.50.121:8118',
            '120.55.61.182:80',
            '116.199.2.197:82',
            '114.215.102.168:8081',
            '115.159.0.178:808'
        ]
        pass

    # 发送请求获取响应
    def get_original_data(self, url):
        proxy = {'http': random.choice(self.proxy_list)}
        response = requests.get(url, headers=self.headers)
        # 得到响应数据
        self.original_data = response.content.decode()

    # 数据的处理
    def handle_original_data(self):
        # 将json数据转换为字典
        self.dict_data = json.loads(self.original_data)
        print(self.dict_data)
        # 获取我们需要的数据存放到一个列表中
        self.data_list = list()
        for i in self.dict_data['data']:
            temp = dict()
            temp['title'] = i['title']
            temp['url'] = 'https://www.toutiao.com/a' + i['source_url'].split('/')[2]
            self.data_list.append(temp)
        # 获取下次请求用的max_behot_time参数的值
        max_behot_time = self.dict_data['next']['max_behot_time']
        return max_behot_time

    def get_signature(self, user_id):
        """
        计算_signature
        :param user_id: user_id不需要计算，对用户可见
        :return: _signature
        """
        req = requests.Session()
        # 创建驱动
        driver = webdriver.Chrome()
        # js获取目的
        js_url = 'https://s3.pstatp.com/toutiao/resource/ntoutiao_web/page/profile/index_8f8a2fb.js'
        resp = req.get(js_url, headers=self.headers)
        js = resp.content.decode()
        effect_js = js.split("Function")
        js = 'var navigator = {};\
            navigator["userAgent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36";'+ "Function" + effect_js[3] + "Function" + effect_js[4] + ";function result(){ return TAC.sign(" + user_id + ");} result();"
        # JS执行步骤
        vl5x = driver.execute_script(js)

        return vl5x


    # 数据的保存
    def save_data(self):
        for data in self.data_list:
            # 将数据转换为json数据格式写入文件
            con_str = json.dumps(data, ensure_ascii=False)
            self.file.write(con_str + ',\n')
            pass
        pass

    # 函数的运行开始方法
    def run(self):
        # 发送请求获取响应
        self.get_original_data(self.web_index_url)
        # 解析响应数据获取我们所需的信息
        max_behot_time = self.handle_original_data()
        # 判断是否要对数据二次处理
        # 得到最终要保留的数据
        # 将数据写入本地文件中
        self.save_data()
        while max_behot_time:
            # 休息一段随机时间
            time.sleep(random.randint(2,6))
            # 得到签名
            # vl5x = self.get_signature(user_id)
            vl5x = self.get_signature('1243')
            # 得到下一次的url
            url = self.web_after_url.format(max_behot_time, vl5x)
            # 发送请求获取响应
            self.get_original_data(url)
            # 解析响应数据获取我们所需的信息
            max_behot_time = self.handle_original_data()
            # 判断是否要对数据二次处理
            # 得到最终要保留的数据
            # 将数据写入本地文件中
            self.save_data()
            pass
        pass

    # 用于功能结束后的清理工作
    # def __del__(self):
    #     # 关闭文件
    #     self.file.close()
    #     pass



if __name__ == '__main__':
    toutiao = TouTiao()
    toutiao.run()