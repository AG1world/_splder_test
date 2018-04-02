# 代理池测试
import requests
from random import choice

proxy_list = ["101.254.196.239:3128",
"101.37.79.125:3128",
"101.53.101.172:9999",
"106.122.171.0:8118",
"111.197.160.17:8118",
"112.86.140.218:8888",
"112.95.91.40:9999",
"114.228.90.113:6666",
"116.199.115.78:80",
"118.144.187.254:3128",
"119.190.34.70:80",
"119.249.48.235:80",
"119.28.99.194:3128",
"119.49.144.83:80",
"120.26.160.183:8090",
"120.92.102.240:10000",
"122.152.219.158:8080",
"122.245.15.134:6666",
"123.207.150.111:8888",
"14.118.252.152:6666",
"14.118.252.237:6666",
"14.118.254.165:6666",
"149.56.36.132:80",
"166.111.80.162:3128",
"180.141.8.204:8118",
"183.30.197.151:9797",
"185.112.180.249:8080",
"190.2.133.214:1080",
"190.2.133.215:1080",
"190.2.133.218:1080",
"209.50.52.199:9000",
"210.5.149.43:8090",
"218.28.131.34:3128",
"218.59.139.238:80",
"37.204.202.218:8081",
"58.82.151.37:8080",
"60.2.148.253:80",
"60.205.125.201:8888",
"60.205.228.133:9999",
"60.208.44.228:80",
"71.13.112.152:3128",
"80.211.169.36:80",
"89.236.17.108:3128"]
def get_ip(proxy_list):

    ip = choice(proxy_list)
    proxy = {
        'http':'http://' + ip,
        'https':'https//' + ip
    }
    print(proxy)
    return proxy

def test_con(proxy) :

    url = 'https://www.baidu.com'
    count = 0
    while count<5:
        try:
            response = requests.get(url,proxies = proxy, timeout = 3).content.decode()
            print(response)
        except:
            get_ip(proxy_list)
            count += 1
    print('请求次数过多,无可用ip')
proxy = get_ip(proxy_list)
test_con(proxy)