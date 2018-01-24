# -*- coding:utf-8 -*-
import requests

#通过cookie获取需要权限的信息
#cookie在headers中

# 构建url
url ='http://www.renren.com/PLogin.do'
# 构建ｈｅａｄｅｒｓ
headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',

}
# 构建表单数据
post_data ={
    'email':'17173805860',
    'password':'1qaz@WSX3edc'
}
# 发送请求 获取响应
session = requests.session()
session.post(url,headers=headers,data=post_data)
# 验证的登录
response = session.get('http://www.renren.com/923768535')

print(response.content.decode())