# -*- coding: utf-8 -*-
from selenium import webdriver
import time

# 构建url
url = 'https://zc.yy.com/reg/udb/reg4udb.do?appid=5614&action=3&type=Mobile&mode=udb&busiurl=http%3A%2F%2Fwww.zhiniu8\
.com%2F&reqDomainList=lgn.zhiniu8.com,lgn.yy.com,lgn.duowan.com&fromadv=www.zhiniu8.com'
# 构建浏览器对象
dr = webdriver.Chrome()

# 加载响应获取url
dr.get(url)


# # 定位注册
el_reg = dr.find_element_by_xpath('//*[@id="reg_btn"]')
el_reg.click()

# 跳入框架内
el_1 = dr.find_element_by_xpath('//*[@id="registerIframe"]')
dr.switch_to.frame(el_1)

# dr.implicitly_wait(10)

# 定位账户
# el_user = dr.find_element_by_xpath('//*[@id="m_mainForm"]/div/div[2][@class="form_item passport_item"]/span[2]')
# el_user.send_keys('15921917082')
#
# # # 定位注册
# el_login = dr.find_element_by_xpath('//*[@id="m_mainForm"]/div/div[9]/a/span')