# -*- coding:utf-8 -*-
import  requests

# 构建url
url = 'http://www.baidu.com'
# 构建headers
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
# 获取响应
resp= requests.get(url,headers=headers)

# 将cookie对象转换成字典
dict_cookies = requests.utils.dict_from_cookiejar(resp.cookies)
print(dict_cookies)

# 将字典转换称cookiesjar对象cookies
cookies_jar = requests.utils.cookiejar_from_dict(dict_cookies)
print(cookies_jar)

# 获取cookie
cookie_dict = resp.cookies.get_dict()
print(cookie_dict)

cookie = resp.cookies
print(cookie)

response = requests.get('http://www.baidu.com')
print(response.status_code)
assert response.status_code == 300