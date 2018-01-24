# -*- coding:utf-8 -*-

#将cookies中值以字典形式存在cookies大字典中
import requests

# 构建url
url ='http://www.renren.com/923768535'

# 构建请求头

headers ={
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
# 获取cookie
temp = 'anonymid=jcg8efxs-8gio4q; depovince=GW; _r01_=1; JSESSIONID=abcmiPGgvWusffR5q95dw; jebecookies=e14a9b38-32b1-403b-8bb9-678cac467be6|||||; ick_login=e440eea5-0d19-456f-a161-06ef05e10674; _de=4F1FF60C280AA48B2CD1201DB4C6DF4A; p=7396aebb49bf23a503edecb50f89381e5; first_login_flag=1; ln_uact=17173805860; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=a9a4ba838a55a3116a9867eec11a62fc5; societyguester=a9a4ba838a55a3116a9867eec11a62fc5; id=923768535; xnsid=5fc2083; ch_id=10050; ver=7.0; loginfrom=null; wp_fold=0'
# cookies = {}
# for i in temp.split('; '):
#     cookies[i.split('=')[0]] = i.split('=')[1]
# 列表生成式
cookies = {i.split('=')[0]:i.split('=')[1]for i in temp.split('= ')}
response = requests.get(url,cookies=cookies,headers=headers)

print(response.content.decode())
