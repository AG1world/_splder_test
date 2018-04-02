import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""
https://www.huxiu.com/

https://www.huxiu.com/v2_action/article_list

https://www.huxiu.com/v2_action/article_list


https://api.growingio.com/v2/b6a739d69e7ea5b6/web/action?stm=1520170748614
https://api.growingio.com/v2/b6a739d69e7ea5b6/web/action?stm=1520170758832

"""

import requests

driver = webdriver.Chrome()

driver.get('https://www.huxiu.com/')



el = driver.find_element_by_xpath('//*[@id="index"]/div[1]/div[3]')
el.click()
time.sleep(5)
# element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.xpath())))

d = driver.find_element_by_xpath('//*[@id="index"]/div[1]/div[2]/div[53]/div[3]/h2/a').text

print(d)
