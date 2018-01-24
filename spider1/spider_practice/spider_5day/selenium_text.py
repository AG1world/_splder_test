import time
from selenium import webdriver


from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# 如果没有在环境变量指定PhantomJS位置
# driver  = webdriver.PhantomJS(executable_path="./phantomjs")

driver.get('http://www.baidu.com')

data = driver.find_element_by_id('wrapper').text

#打印数据内容

print(data)
print(driver.title)

driver.save_screenshot('baidu.png')

