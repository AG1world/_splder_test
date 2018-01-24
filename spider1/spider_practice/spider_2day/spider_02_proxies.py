# -*- coding:utf-8 -*-
import requests

# 使用代理

# 构建url
url = 'https://www.baidu.com'

# 构建headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

proxies = {
    'http':'http://101.201.79.172:808',
    'https':'http://101.201.79.172:808'
}

# 私密代理
# proxies = {
#     "http": "http://morganna_mode_g:ggc22qxp@117.48.214.246:16816",
#     "https": "https://morganna_mode_g:ggc22qxp@117.48.214.246:16816",
# }
# 获请求响应
response = requests.get(url,headers = headers,timeout=10,proxies=proxies)
print(response.content)

