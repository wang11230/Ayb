# !/usr/bin/python
# -*-coding:utf-8 -*-
from time import sleep
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.cugbonline.cn/index.do')
sleep(3)
# 进入iframe框架
browser.switch_to.frame(browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[3]/div/div[2]/iframe'))
print('获取登陆框架...')
browser.find_element_by_name('username').send_keys('1929010120368')
browser.find_element_by_id('password').send_keys('140106198709170631')
sleep(1)
print('休息5秒后自动登陆...')
sleep(5)
browser.find_element_by_name('submit').click()

for i in range(120):
    try:
        el = browser.find_element_by_link_text('我的课程')
        if el.is_displayed():
            break
    except:
        pass
    sleep(3)

browser.find_element_by_link_text('我的课程')
browser.find_element_by_link_text('我的课程').click()
print('登陆成功，进入“我的课程”页面...')
print('正在获取全部课程信息...')
sleep(15)
browser.switch_to.frame('main')
browser.find_element_by_link_text('计算机组成原理').click()
print('已打开“计算机组成原理”课程页面...')
# 获取所有窗口句柄,打开新页面后，返回到首页。
window_handles = browser.window_handles
browser.switch_to.window(window_handles[0])
sleep(2)
browser.switch_to.frame('main')
browser.find_element_by_link_text('Windows程序设计').click()
print('已打开“Windows程序设计”课程页面...')
window_handles = browser.window_handles
browser.switch_to.window(window_handles[0])
sleep(2)
browser.switch_to.frame('main')
browser.find_element_by_link_text('计算机系统结构').click()
print('已打开“计算机系统结构”课程页面...')
window_handles = browser.window_handles
browser.switch_to.window(window_handles[0])
browser.switch_to.frame('main')
sleep(2)
browser.find_element_by_link_text('计算机图形学').click()
print('已打开“计算机图形学”课程页面...')
window_handles = browser.window_handles
browser.switch_to.window(window_handles[0])
sleep(2)
# 标签页重新赋值
print('课程标签页重新赋值中...')
browser.switch_to.window(window_handles[1])
browser.get(
    'http://jiaoxue.cugbonline.cn/meol/microlessonunit/viewMicroLessnMulti.do?courseId=10103&mluId=13488&ustats=unit')
sleep(10)
browser.switch_to.window(window_handles[2])
browser.get(
    'http://jiaoxue.cugbonline.cn/meol/microlessonunit/viewMicroLessnMulti.do?courseId=10909&mluId=52147&ustats=unit')
sleep(10)
browser.switch_to.window(window_handles[3])
browser.get(
    'http://jiaoxue.cugbonline.cn/meol/microlessonunit/viewMicroLessnMulti.do?courseId=11460&mluId=13794&ustats=unit')
sleep(10)
browser.switch_to.window(window_handles[4])
browser.get(
    'http://jiaoxue.cugbonline.cn/meol/microlessonunit/viewMicroLessnMulti.do?courseId=10438&mluId=14081&ustats=unit')
sleep(10)
print('10秒后进入挂机...')

while True:
    a = 1
    b = 10
    window_handles = browser.window_handles
    if a < b:
        browser.switch_to.window(window_handles[1])
        browser.refresh()
        sleep(5)
        browser.find_element_by_id('resAct_min')
        browser.find_element_by_id('resAct_min').click()
        t = time.strftime("%H:%M:%S", time.localtime())
        print('【' + t + '】' + '刷新【计算机组成原理】...')
        sleep(5)
        browser.switch_to.window(window_handles[2])
        browser.refresh()
        sleep(5)
        browser.find_element_by_id('resAct_min')
        browser.find_element_by_id('resAct_min').click()
        t = time.strftime("%H:%M:%S", time.localtime())
        print('【' + t + '】' + '刷新【Windows程序设计】...')
        sleep(5)
        browser.switch_to.window(window_handles[3])
        browser.refresh()
        sleep(5)
        browser.find_element_by_id('resAct_min')
        browser.find_element_by_id('resAct_min').click()
        t = time.strftime("%H:%M:%S", time.localtime())
        print('【' + t + '】' + '刷新【计算机系统结构】...')
        sleep(5)
        browser.switch_to.window(window_handles[4])
        browser.refresh()
        sleep(5)
        browser.find_element_by_id('resAct_min')
        browser.find_element_by_id('resAct_min').click()
        t = time.strftime("%H:%M:%S", time.localtime())
        print('【' + t + '】' + '刷新【计算机图形学】...')
        sleep(5)
        browser.switch_to.window(window_handles[0])
        browser.refresh()
        t = time.strftime("%H:%M:%S", time.localtime())
        print('【' + t + '】' + '返回首页...20分钟后再次执行...')
        sleep(5)
    else:
        break
    sleep(1200)
# sleep(2)
# browser.quit()
