
import requests
import os
kw = {'wd':'长城'}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

# response = requests.get("http://www.baidu.com/s?",params = kw,headers =headers)
# text = response.text

# with open('text.txt','w') as f:
#     f.write(text)

# content = response.content.decode("utf-8")

# with open('content.txt','w') as f:
#     f.write(content)

print('>>>>>1')


# print(response.url)
# print(response.encoding)
# print(response.status_code)

print('>>>>>2')
from io import BytesIO
f = BytesIO()
#写入是utf-8编码的二进制文件
f.write('中文'.encode('utf-8'))
# 获得写入的数据
print(f.getvalue())
# 因为数据末尾,不能得到后面仍和数据
print(f.read())
f.seek(0)
f.write(b'123')
#utf-8中文占3个字节
print(f.getvalue())

# a = open("a.txt",'w')
# a.write('aaaaaa\nbbbb1')
# a.close()
f = open("a.txt",'r')
print('_____')
for i in f.readlines():
    print(i.strip())
    print(f.tell())
# f.seek(1,0) ,只有文件是以二进制读取时,才可以在从非文件头开始计算相对位置
# print('_____')
# f.seek(0)
# # f.seek(2,1)
# print(f.tell())
# f.seek(0,2)
# print(f.tell())






# 写的三要素 打开 写入 关闭
# 没有文件.创建文件,有内容,清除内容,重新写入
# 创建文件是以当前"运行程序文件"文件夹下,创建文件

# f = open('content1.txt','w')
# f.write('dongdong caiji')
# f.close()

# 读取大文件,
# 1.在不清楚文件大小,逐行读取
# 2.read("size")<最多读取的大小>
# file1 = open('content1.txt','r')
# lines = file1.readlines()
# for line in lines:
#     print(line.strip())





