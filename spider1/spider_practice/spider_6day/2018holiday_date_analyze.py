# -*- coding:utf-8 -*-

# f获取网址，得到文本数据
# 解析数据结构，使用什么方法获取更简单
#1. 数据格式不清楚，先打印看看
#2. 先写出最先出结果的程序
#3. append（） 是往列表添加元素（传入数据，即字符串后者列表等）
#4. +=  当元素是列表时，是在列表中拼接元素


# <time datetime="2018-04-05" class="dtstart" style="display: none;">2018-04-05</time>

import requests,re
import datetime


url = 'https://publicholidays.cn/zh/2018-dates/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'

}
response = requests.get(url,headers=headers)
# 写入文件的数据必须是字符串的形式或者json格式
# with open('date_2018','w') as f:
#     f.write(response.content.decode())

# 解析数据
tbody = re.findall(r'<tbody>(.*?)</tbody>',response.text)[0]


# 遍历tbody中tr，获取tr中date,summary数据
tr_list = re.findall(r'<tr class=.*?>(.*?)</tr>',tbody)
print(len(tr_list))

pattern1 = re.compile('<time datetime=.*?>(\d+-\d+-\d+)</time>')
pattern2 = re.compile('<a .*?>(.*?)</a>')

for tr in tr_list:
    result = pattern1.findall(tr)

    fesitival = pattern2.findall(tr)

    try:
        fesitival_name=fesitival[0]
    except:
        fesitival_name = '元旦'

    if len(result)==1:
        days=1

        date = result[0]
        print('{}日期为{}'.format(fesitival_name, result[0]))
    else:
        # ['2018-04-29', '2018-05-01']
        new_list =[]
        for temp in result:
            new_list += temp.split('-')
        # print(new_list)
        d1 = datetime.date(int(new_list[0]), int(new_list[1]),int(new_list[2]))
        d2 = datetime.date(int(new_list[-3]), int(new_list[-2]), int(new_list[-1]))
        days = (d2-d1).days+1
        print('{}日期为{}至{}'.format(fesitival_name,result[0],result[1]))
    print (days)

        # for num_list in result:
        #     num_list =num_list.split('-')
        #     for a,b,c in num_list:
        #         y = a
        #         m = b
        #         d = c
        #         date = (y,m,d)
        # date_num = [ num_list.split('-')for num_list in result]
        # print(date_num)


# import datetime
#
# d1 = datetime.date(2015, 10, 7)
# d2 = datetime.date(2015, 8, 15)
# print((d1 - d2).days)







# tr [] ,元素为7
# tr_list = [['2018','1','20'],['2018','2','10']]
#
# new_list = []
# for tr in tr_list:
#     new_list += tr
#     print(new_list)
#

list1 = []
new_list = ['123',['1']]
for i in new_list:
    print(i)
    list1 +=i
    print(list1)


