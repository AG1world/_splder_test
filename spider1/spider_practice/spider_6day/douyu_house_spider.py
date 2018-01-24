# https://www.douyu.com/directory/all

# 斗鱼爬取房间号，
import json
import time

room_name='./a/div/p/span[1]'
visit_num = './a/div/p/span[2]'
image ='./a/span/img'
# data_rid ='./a/@href'[xpath]  ; data_rid ='./aattribute('href) selenium
category = './div/div/span'

node = '//*[@id="live-list-contentbox"]/li/a'


from selenium import webdriver

class DouYu(object):
    def __init__(self):

        self.driver = webdriver.Chrome()
        # 请求首页，通过浏览器打开制定首页
        self.driver.get('http://www.douyu.com/directory/all')
        self.file = open('douyu.json','w')

    def get_data(self):
        time.sleep(3)
        el_list = self.driver.find_elements_by_xpath('//*[@id="live-list-contentbox"]/li')
        print(el_list)
        data_list = []
        for el in el_list:
            temp = {}
            temp['room_name'] = el.find_element_by_xpath('./a/div/p/span[1]').text
            temp['visit_num'] = el.find_element_by_xpath('./a/div/p/span[2]').text
            temp['image'] = el.find_element_by_xpath('./a/span/img').get_attribute('data-original')
            temp['category'] = el.find_element_by_xpath('./a/div/div/span').text
            print(temp)
            data_list.append(temp)

        return data_list
    def save_data(self,data_list):
        for data in data_list:
            data_json = json.dumps(data,ensure_ascii=False) + ',\n'
            self.file.write(data_json)



    def run(self):
        # 请求首页，通过浏览器打开指定首页
        #通driver打开首页，并且通过xpath定位节点列表
        data_list  = self.get_data()
        # 遍历节点列表，将每个节点数据存在响应的字典中，再通过新列表装填
        # 遍历新列表，得到字典数据，在dumps ，转化json数据，存储
        #运行实例化方法，得到一整页面后，通过定位到下一页节点，循环获取，当获取不下一页节点，即可终止程序
        self.save_data(data_list)

        # '<a href="#" class="shark-pager-next">下一页</a>'
        # 下一页请求只能通过ajaxk出发
        # xpath   == //*[@id="J-pager"]/a[11]

        while self.driver.find_element_by_xpath ('//*[@id="J-pager"]/a[11]'):
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="J-pager"]/a[last()-1]').click()
            # time.sleep(3)
            data_list = self.get_data()
            self.save_data(data_list)

    # def __del__(self):
    #     self.file.close()

if __name__ == '__main__':
    douyu = DouYu()
    douyu.run()

