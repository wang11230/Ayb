# !/usr/bin/python
# -*-coding:utf-8 -*-
from selenium import webdriver
from time import sleep
import datetime
from datetime import datetime
import pytz
import time
import os
from os import path

d = path.dirname(__file__)
abspath = path.abspath(d)
browser = webdriver.Chrome()
# browser.maximize_window()

tz = pytz.timezone('Asia/Shanghai')


# 登陆函数
def login():
    browser.get('https://www.taobao.com/')
    for i in range(30):
        try:
            el = browser.find_element_by_link_text('亲，请登录')
            if el.is_displayed():
                break
        except:
            pass
        sleep(1)
    else:
        print('等待触发登陆已超时...关闭浏览器，脚本已停止。')
        browser.close()

    browser.find_element_by_link_text('亲，请登录')
    browser.find_element_by_link_text('亲，请登录').click()
    print('触发登录事件...')

    for i in range(30):
        try:
            el = browser.find_element_by_xpath('//*[@id="login"]/div[1]/i')
            if el.is_displayed():
                break
        except:
            pass
        sleep(1)
    else:
        print('等待登陆二维码超时...关闭浏览器，脚本已停止。')
        browser.close()

    browser.find_element_by_xpath('//*[@id="login"]/div[1]/i')
    browser.find_element_by_xpath('//*[@id="login"]/div[1]/i').click()
    print('请在30秒内完成扫码登陆...')

    for i in range(30):
        try:
            el = browser.find_element_by_id('J_MiniCart')
            if el.is_displayed():
                break
        except:
            pass
        sleep(1)
    else:
        print('购物车页面等待超时...关闭浏览器，脚本已停止。')

    browser.find_element_by_id('J_MiniCart')
    browser.find_element_by_id('J_MiniCart').click()
    print('跳转至购物车页面...')

    for i in range(30):
        try:
            el = browser.find_element_by_id('J_SelectAll1')
            if el.is_displayed():
                break
        except:
            pass
        sleep(1)
    else:
        print('勾选商品等待超时...关闭浏览器，脚本已停止。')
    browser.find_element_by_id('J_SelectAll1')
    browser.find_element_by_id('J_SelectAll1').click()
    print('勾选商品，等待提交订单...')


# 购买函数
def buy(buytime):
    while True:
        # 获取实时北京时间
        t = datetime.fromtimestamp(int(time.time()),
                                   tz).strftime('%Y-%m-%d %H:%M:%S %Z%z')
        # 对比时间，如果北京时间大于设定时间，点击提交订单。
        # 反之循环获取对比。2020年11月9日17:37:11
        if t > buytime:
            try:
                # 点击结算按钮
                if browser.find_element_by_id('J_Go'):
                    browser.find_element_by_id('J_Go').click()
                browser.find_element_by_link_text('提交订单').click()
            except:
                sleep(0.1)
        print(t)
        sleep(0.1)


if __name__ == "__main__":
    login()
    buy('2020-11-13 10:07:00.392000')
