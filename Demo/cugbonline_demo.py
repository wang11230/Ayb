# !/usr/bin/python
# -*-coding:utf-8 -*-
from time import sleep
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.cugbonline.cn/index.do')
# browser.maximize_window()
sleep(3)
# 进入iframe框架
browser.switch_to.frame(browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[3]/div/div[2]/iframe'))
print('获取登陆框架...')
browser.find_element_by_name('username').send_keys('1929010120368')
browser.find_element_by_id('password').send_keys('140106198709170631')
sleep(1)
browser.find_element_by_name('submit').click()
print('自动登陆中...')
for i in range(30):
    try:
        el = browser.find_element_by_link_text('我的课程')
        if el.is_displayed():
            break
    except:
        pass
    sleep(1)
browser.find_element_by_link_text('我的课程').click()
print('登陆成功，进入“我的课程”页面...')
sleep(6)

print('正在获取全部课程信息...')
sleep(2)
browser.switch_to.frame('main')
browser.find_element_by_link_text('计算机组成原理').click()
print('已打开“计算机组成原理”课程页面...')
# 获取所有窗口句柄
window_handles = browser.window_handles
# 切换回第一标签
browser.switch_to.window(window_handles[0])
sleep(2)
browser.switch_to.frame('main')
browser.find_element_by_link_text('Windows程序设计').click()
print('已打开“Windows程序设计”课程页面...')
window_handles = browser.window_handles
# 切换回第一标签
browser.switch_to.window(window_handles[0])
sleep(2)
browser.switch_to.frame('main')
browser.find_element_by_link_text('计算机系统结构').click()
print('已打开“计算机系统结构”课程页面...')
window_handles = browser.window_handles
# 切换回第一标签
browser.switch_to.window(window_handles[0])
browser.switch_to.frame('main')
sleep(2)
browser.find_element_by_link_text('计算机图形学').click()
print('已打开“计算机图形学”课程页面...')
window_handles = browser.window_handles
# 切换回第一标签
browser.switch_to.window(window_handles[0])
print('检测中...')
sleep(2)
print('全部课程页面已就绪，读取挂机配置...')
sleep(5)
print("读取成功...5秒钟后开始挂机...")

while True:
    a = 1
    b = 10
    window_handles = browser.window_handles
    if a < b:
        browser.switch_to.window(window_handles[1])
        browser.refresh()
        browser.find_element_by_link_text('课程学习')
        browser.find_element_by_link_text('课程学习').click()
        sleep(1)
        browser.find_element_by_link_text('播课单元')
        browser.find_element_by_link_text('播课单元').click()
        t = time.strftime("%H:%M:%S", time.localtime())
        print('【' + t + '】' + '刷新【计算机组成原理】...进入播课单元...')
        sleep(5)
        browser.switch_to.window(window_handles[2])
        browser.refresh()
        browser.find_element_by_link_text('课程学习')
        browser.find_element_by_link_text('课程学习').click()
        sleep(1)
        browser.find_element_by_link_text('学习笔记')
        browser.find_element_by_link_text('学习笔记').click()
        t = time.strftime("%H:%M:%S", time.localtime())
        print('【' + t + '】' + '刷新【Windows程序设计】...进入学习笔记...')
        sleep(5)
        browser.switch_to.window(window_handles[3])
        browser.refresh()
        browser.find_element_by_link_text('课程学习')
        browser.find_element_by_link_text('课程学习').click()
        sleep(1)
        browser.find_element_by_link_text('答疑讨论')
        browser.find_element_by_link_text('答疑讨论').click()
        t = time.strftime("%H:%M:%S", time.localtime())
        print('【' + t + '】' + '刷新【计算机系统结构】...进入答疑讨论...')
        sleep(5)
        browser.switch_to.window(window_handles[4])
        browser.refresh()
        browser.find_element_by_link_text('课程学习')
        browser.find_element_by_link_text('课程学习').click()
        sleep(1)
        browser.find_element_by_link_text('平时作业')
        browser.find_element_by_link_text('平时作业').click()
        t = time.strftime("%H:%M:%S", time.localtime())
        print('【' + t + '】' + '刷新【计算机图形学】...进入平时作业...')
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
