# !/usr/bin/python
# -*-coding:utf-8 -*-
from selenium import webdriver
from time import sleep
import datetime
from os import path

d = path.dirname(__file__)
abspath = path.abspath(d)
browser = webdriver.Chrome()


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
        t = str(datetime.datetime.now())
        if t < buytime:
            print(t + '--时间比对中...')
        else:
            # 点击结算
            browser.find_element_by_id('J_Go')
            browser.find_element_by_id('J_Go').click()
            for i in range(30):
                try:
                    el = browser.find_element_by_link_text('提交订单')
                    if el.is_displayed():
                        break
                except:
                    pass
                sleep(0.1)
            browser.find_element_by_link_text('提交订单')
            browser.find_element_by_link_text('提交订单').click()
            print('开始提交订单...')
            break
        sleep(1)

if __name__ == "__main__":
    login()
    buy('2020-11-13 16:06:00.392000')
