# !/usr/bin/python
# -*-coding:utf-8 -*-
from selenium import webdriver
from time import sleep
import requests
import os
driver = webdriver.Firefox()
driver.get('https://www.bphc.com.cn/front/member/toLogin')
sleep(1.5)
driver.maximize_window()
driver.find_element_by_class_name('click_form_pwd').click()
sleep(2)
url = driver.find_element_by_id('captcha_img').get_attribute('src')
print(url)
sleep(2)
driver.get(url)
#driver.quit()
