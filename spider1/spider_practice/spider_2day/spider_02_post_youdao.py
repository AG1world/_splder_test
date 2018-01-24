# -*- coding:utf-8 -*-
import json

import requests
import sys



class Translator(object):
    def __init__(self,word):
        # 构建参数
        self.word = word
        # 构建响应头
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
        # 构造url
        # request请求网址,少了参数 http: // fanyi.youdao.com / translate_o?smartresult = dict & smartresult = rule
        self.url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
        self.post_data = {
            'i': self.word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': '1515938107792',
            'sign': '50c1d8d43ce194e29ce8bbf57ce879e4',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTIME',
            'typoResult': 'false',
        }
     # 返回响应数据str
    def get_response(self):
        response = requests.post(self.url,headers=self.headers,data = self.post_data)
        print(response.json())
        content= response.content.decode('utf-8')
        # print(content)
        return content
    # 将获取的json数据转换成python字典 数据显示数据
    def parse_data(self,content):
        data = json.loads(content)
        print('>>>>>>>')
        print(data['translateResult'][0][0]['tgt'])
    def run(self):
        content = self.get_response()
        self.parse_data(content)


if __name__ == '__main__':
    word=sys.argv[1]
    translator = Translator(word)
    translator.run()