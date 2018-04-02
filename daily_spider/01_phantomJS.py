# 导包
from selenium import webdriver
# 创建 驱动对象
driver = webdriver.PhantomJS()

driver.get('http://www.baidu.com')
print(driver.title)