# -*- coding:utf-8 -*-


# 通过添加cookie信息登录人人网

# 构建url
import requests

url ='http://www.renren.com/923768535'
#构建headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Cookie':'anonymid=jcg8efxs-8gio4q; depovince=GW; _r01_=1; JSESSIONID=abcmiPGgvWusffR5q95dw; jebecookies=bd970bb8-d9c4-4479-b2ab-8171c56aedc4|||||; ick_login=e440eea5-0d19-456f-a161-06ef05e10674; _de=4F1FF60C280AA48B2CD1201DB4C6DF4A; p=c5854894c615b0a00334335598b3b8985; first_login_flag=1; ln_uact=17173805860; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=c17e869394651e3bc4d864bcb614d5e85; societyguester=c17e869394651e3bc4d864bcb614d5e85; id=923768535; xnsid=2fe2a76; ch_id=10050; ver=7.0; loginfrom=null; wp_fold=0'
}
# 获取响应
resp = requests.get(url,headers=headers)
print(resp.content.decode())