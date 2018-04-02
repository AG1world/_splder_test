#coding:utf-8
from selenium import webdriver
import pytesseract
from PIL import Image
import requests

url = 'https://accounts.douban.com/login'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

dr = webdriver.Chrome()

dr.get(url)

# 定位账号输入框元素
el_user = dr.find_element_by_id('email')
el_user.send_keys('m17173805860@163.com')

# 定位密码输入框元素
el_pwd = dr.find_element_by_id('password')
el_pwd.send_keys('1qaz@WSX3edc')

# 定位验证码输入框元素
el_captcha_input = dr.find_element_by_id('captcha_field')
# 1 手动输入
# captcha = input('请输入验证码:')
# el_captcha_input.send_keys(captcha)

# 2.图像识别引擎
# 定位到验证码元素
el_captcha = dr.find_element_by_id('captcha_image')
# 获取验证码图片的url
captcha_url = el_captcha.get_attribute('src')
print(captcha_url)
# 下载保存验证码图片
data = requests.get(captcha_url,headers=headers).content
with open('temp.jpg', 'wb')as f:
    f.write(data)
# 使用图像识别引擎识别验证码图片中的数据
im = Image.open('temp.jpg')
captcha = pytesseract.image_to_string(im)
print('--', captcha, '--')
# 输入验证码
el_captcha_input.send_keys(captcha)


# 定位登录按钮元素
el_submit = dr.find_element_by_name('login')
el_submit.click()