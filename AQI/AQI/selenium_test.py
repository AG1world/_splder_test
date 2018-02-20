#coding:utf-8



# selenium 自动化测试
import time
from selenium import webdriver

url = 'https://www.aqistudy.cn/historydata/daydata.php?city=%E6%B2%A7%E5%B7%9E&month=201607'

# 创建一个浏览器对象
dr = webdriver.Chrome()
# 访问url
dr.get(url)
time.sleep(3)
# 定位搜索输入框
# el = dr.find_element_by_id('kw')
# el = dr.find_element_by_name('wd')
# 输入关键词
# el.send_keys('python')
# 定位到搜索按钮
# el_sub = dr.find_element_by_id('su')
# 点击搜索按钮
# el_sub.click()

# link_text使用
# el = dr.find_element_by_link_text('hao123')
# el = dr.find_element_by_partial_link_text('hao')
# css_selector
data = dr.page_source.encode()
print(data)
dr.close()